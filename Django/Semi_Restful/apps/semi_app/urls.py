from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^semi_app$', index),
    url(r'^semi_app/new$', new),
    url(r'^semi_app/create$', create),
    url(r'^semi_app/(?P<user_id>\d+)/edit$', edit),
    url(r'^semi_app/(?P<user_id>\d+)/update$', update),
    url(r'^semi_app/(?P<user_id>\d+)/delete$', delete),
    url(r'^semi_app/(?P<user_id>\d+)$', show),
]

