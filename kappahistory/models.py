import json
import datetime as dt
from django.db import models

class KappaSponsorship(models.Model):
    player = models.ForeignKey('Player')
    event = models.ForeignKey('Event')
    result = models.PositiveIntegerField()
    drives = models.ManyToManyField('Drive', null=True, blank=True)
    game = models.ForeignKey('Game', null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.player, self.event)

    @property
    def has_happened(self):
        return dt.date.today() > self.event.end

class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    start = models.DateField()
    end = models.DateField()
    name = models.CharField(max_length=500)
    location = models.ForeignKey('Location')

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.ForeignKey('City')
    state = models.ForeignKey('State')
    country = models.ForeignKey('Country')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return ', '.join(map(str, [self.city, self.state, self.country]))

    @property
    def map_json(self):
        sponsorships = KappaSponsorship.objects.all() \
                            .filter(event__location=self)

        json_data = {
                'location': str(self),
                'coords': [self.longitude, self.latitude],
                'sponsorships': [{
                    'event': str(s.event),
                    'player': str(s.player),
                    'result': str(s.result),
                    'game': str(s.game)} for s in sponsorships]
                }

        return json_data

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Drive(models.Model):
    url = models.URLField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class VideoHighlight(models.Model):
    video_id = models.CharField(max_length=200)
    kappasponsorship = models.ForeignKey('KappaSponsorship')

