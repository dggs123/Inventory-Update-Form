from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
			url('^$', index, name='home'),
			url('^play/(?P<id>\d+)/$', play, name='play'),

			]