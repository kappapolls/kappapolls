import json, os, re
from django.core.management.base import BaseCommand, CommandError
from polls.utils import KappaPollsBot
from polls.models import Poll, Vote, KappaUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        # query.values_list('value') returns like [(1,), (2,), (3,)]
        f = lambda x: x[0]

        active_polls = Poll.objects.filter(status__name='Active')

        for poll in active_polls:
            choices = map(f, poll.choice_set.values_list('name'))
            voted_comments = map(f, poll.choice_set.values_list('vote__comment_id'))
            voted_users = map(f, poll.choice_set.values_list('vote__user_id'))

            kappabot = KappaPollsBot()
            vote_thread = kappabot.r.get_submission(submission_id=poll.thread_id)
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


