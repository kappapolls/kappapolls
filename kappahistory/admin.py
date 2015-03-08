from django.contrib import admin
from kappahistory.models import KappaSponsorship, Player, Event, Location, \
        City, State, Country, VideoHighlight, Drive, Game

# Register your models here.
admin.site.register(KappaSponsorship)
admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(VideoHighlight)
admin.site.register(Drive)
admin.site.register(Game)
