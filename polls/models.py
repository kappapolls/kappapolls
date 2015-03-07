import json
from django.db import models
from django.core.exceptions import ValidationError

class Poll(models.Model):
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    thread_id = models.CharField(max_length=256, unique=True)
    status = models.ForeignKey('PollStatus')
    description = models.TextField()
    open_date = models.DateField()
    close_date = models.DateField()

    @property
    def results(self):
        choices = []
        for choice in self.choice_set.all():
            choices.append({choice:  choice.vote_set.count()})
        return choices

    @property
    def json_results(self):
        # merge this with above method at some point
        choices = []
        for choice in self.choice_set.all():
            choices.append({'choice': choice.name,
                            'votes': choice.vote_set.count()})
        return json.dumps(choices)

    @property
    def is_active(self):
        return self.status.name == 'Active'

    def __unicode__(self):
        return self.name

class Choice(models.Model):
    poll = models.ForeignKey('Poll')
    name = models.CharField(max_length=500)

    @property
    def vote_count(self):
        return self.vote_set.filter(user__blacklisted=False).count()

    def __unicode__(self):
        return "%s - %s" % (self.poll, self.name)

class KappaUser(models.Model):
    username = models.CharField(max_length=128, unique=True)
    blacklisted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

class Vote(models.Model):
    user = models.ForeignKey('KappaUser')
    choice = models.ForeignKey('Choice')
    comment_id = models.CharField(max_length=100)

    def validate_unique(self, *args, **kwargs):
        super(Vote, self).validate_unique(*args, **kwargs)
        sibling_choices = self.choice.poll.choice_set

        # values_list returns a list like [(1,), (2,)]
        # made of user ids
        f = lambda x: x[0]
        voters = map(f, sibling_choices.values_list('vote__user'))
        print voters
        if self.user.id in voters:
            raise ValidationError({'user':
                'This user already voted in this poll'})

    def __unicode__(self):
        return "%s - %s - %s" % (self.user, self.choice, self.choice.poll)

class PollStatus(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
