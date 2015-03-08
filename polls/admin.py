from django.contrib import admin
from polls.models import Poll, Choice, KappaUser, Vote, PollStatus

# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(KappaUser)
admin.site.register(Vote)
admin.site.register(PollStatus)
