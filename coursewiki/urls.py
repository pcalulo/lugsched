from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from piston.resource import Resource
from views import *

urlpatterns = patterns('',
    (r'search$', search_view),

    (r'^(?P<uni_name>[^/]+)/actions/addcourse$', add_course_view),

	(r'^$', main_page),
	(r'^(?P<uni_name>[^/]+)/', main_page),
)
