from django.conf.urls import patterns, url
import polls.views as views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),

        url(r'^top_commenters/$',
            views.top_commenters,
            name='top_commenters'),

        url(r'^poll/(?P<poll_thread_id>[a-zA-Z0-9]+)/results/$',
                views.poll_results_json,
                name='poll_results_json'),

        url(r'^poll/(?P<slug>[\w-]+)/$',
            views.poll_detail,
            name='poll_detail')
        )
