from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from piston.resource import Resource
from views import *

urlpatterns = patterns('',
	(r'^$', sched_home),
    (r'canvastest$', direct_to_template, {'template': 'schedules/canvastest.html'}),
)
