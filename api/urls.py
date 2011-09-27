from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import UniversityHandler

uni_handler = Resource(UniversityHandler)

urlpatterns = patterns('',
	(r'^university/(?P<uni_id>[^/]+)/', uni_handler),
	(r'^university/', uni_handler),
)
