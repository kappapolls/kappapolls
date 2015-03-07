from django.conf.urls import patterns, url
import kappahistory.views as views

urlpatterns = patterns('',
    url(r'^$', views.KappaSponsorshipList.as_view(), name='sponsorship_list'),
    )
