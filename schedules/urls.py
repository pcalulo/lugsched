from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from views import *

urlpatterns = patterns('',
	(r'^$', sched_home),
)
