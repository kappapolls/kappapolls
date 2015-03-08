import json, os, re, fcntl, sys
from django.core.management.base import BaseCommand, CommandError
from polls.utils import KappaPollsBot
from polls.models import Poll, Vote, KappaUser


class Command(BaseCommand):

    def try_to_get_lock(self):
        # to keep from multiple processes breaking api rules
        print 'trying to get lock'

        f = os.open('active_polls_lock', os.O_CREAT | os.O_TRUNC | os.O_WRONLY)
        try: fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            #couldnt get lock
            print 'cant lock'
            sys.stderr.write('couldnt get lock')
            sys.exit(-1)
        print 'got lock'
        return True

    def handle(self, *args, **options):

        self.try_to_get_lock()

        # query.values_list('value') returns like [(1,), (2,), (3,)]
        f = lambda x: x[0]

        active_polls = Poll.objects.filter(status__name='Active')

        for poll in active_polls:
            choices = map(f, poll.choice_set.values_list('name'))
            voted_comments = map(f, poll.choice_set.values_list('vote__comment_id'))
            voted_users = map(f, poll.choice_set.values_list('vote__user_id'))

            kappabot = KappaPollsBot()
            vote_thread = kappabot.r.get_submission(submission_id=poll.thread_id)
            vote_thread.replace_more_comments(limit=None)
                
            for comment in vote_thread.comments:
                if comment.id in voted_comments:
                    #skip comments we already looked at
                    continue

                # if a comment has more than one valid vote, then
                # it's no good
                matches = []
                for choice in choices:
                    match = re.search('\+%s' % choice, comment.body, re.IGNORECASE)
                    if match:
                        matches.append(match)

                if len(matches) == 1:
                    # if they only picked one
                    m = matches[0]
                    vote = m.string[m.span()[0]:m.span()[1]].replace('+', '')
                    choice_instance = poll.choice_set.filter(name__iexact=vote).first()

                    # print '%s matched %s' % (vote, comment.body)
                    user, new = KappaUser.objects.get_or_create(
                        username=comment.author.name)

                    # check here to throw out the vote if the user already voted
                    if user.id in voted_users:
                        continue

                    new_vote = Vote(user=user,
                                    comment_id=comment.id,
                                    choice=choice_instance)
                    new_vote.save()


