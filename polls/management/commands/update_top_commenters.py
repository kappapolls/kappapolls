import json, os
from django.core.management.base import BaseCommand, CommandError
from polls.utils import KappaPollsBot

class Command(BaseCommand):


    def handle(self, *args, **options):
        home = os.path.expanduser('~')
        kappabot = KappaPollsBot()
        data = kappabot.top_kappapolls_commenters()
        with open(home + '/kappa/kappapolls/polls/top_commenters.json', 'w') as f:
            f.write(json.dumps(data))

