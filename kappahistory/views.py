import json
from django.shortcuts import render
from django.views.generic import ListView
from kappahistory.models import KappaSponsorship, Location

class KappaSponsorshipList(ListView):
    model = KappaSponsorship
    queryset = KappaSponsorship.objects.all().order_by('-event__start')

    def get_context_data(self, **kwargs):
        context = super(KappaSponsorshipList, self).get_context_data(**kwargs)
        locations = Location.objects.all()
        location_jsons = json.dumps([loc.map_json for loc in locations])
        context['locations'] = location_jsons
        return context
        

