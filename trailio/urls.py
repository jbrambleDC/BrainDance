from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/build_itinerary',
        views.build_itinerary,
        name='build_itinerary')
    url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail')
    url(r'^(?P<user_id>[0-9]+)/itineraries/(?P<itinerary_id>[0-9]+)/$',
        views.itinerary_results,
        name='itinerary_results')
]
