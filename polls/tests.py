from django.test import TestCase
from django.core.exceptions import ValidationError

from polls.models import Poll, Choice, Vote, KappaUser, PollStatus

class PollTests(TestCase):

    def setUp(self):
        PollStatus.objects.create(name='Active').save()
        poll = Poll.objects.create(name='Poll 1',
             thread_id='not important',
             status=PollStatus.objects.get(name='Active'),
             description='no desc',
             open_date='2015-01-01',
             close_date='2016-01-01')

        poll.save()

        choice_1 = Choice.objects.create(name='choice 1', poll=poll)
        choice_2 = Choice.objects.create(name='choice 2', poll=poll)
        choice_1.save()
        choice_2.save()

        for i in range(5):
            user = KappaUser(username='user_%d' % i)
            user.save()

        users = KappaUser.objects.all()
        choices = poll.choice_set.all()

        vote_1 = Vote.objects.create(user=users[0], choice=choices[0])
        vote_1.save()
        vote_2 = Vote.objects.create(user=users[1], choice=choices[0])
        vote_2.save()
        vote_3 = Vote.objects.create(user=users[2], choice=choices[0])
        vote_3.save()
        vote_4 = Vote.objects.create(user=users[3], choice=choices[1])
        vote_4.save()
        vote_5 = Vote.objects.create(user=users[4], choice=choices[1])
        vote_4.save()

    def test_choices_count_votes_correctly(self):

        poll = Poll.objects.get(name='Poll 1')
        users = KappaUser.objects.all()
        choices = poll.choice_set.all()

        self.assertEqual(choices[0].vote_count, 3)
        self.assertEqual(choices[1].vote_count, 2)

    def test_cant_vote_twice(self):

        user1 = KappaUser.objects.first()
        poll = Poll.objects.first()
        choice = poll.choice_set.last()

        with self.assertRaises(ValidationError):
            another_vote = Vote(user=user1, choice=choice)
            another_vote.validate_unique()


