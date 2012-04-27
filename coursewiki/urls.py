from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from piston.resource import Resource
from views import *

urlpatterns = patterns('',
    (r'^(?P<uni_name>[^/]+)/search$', search_view),

    (r'^(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/$', course_details_view),
    (r'^(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/edit$',
        course_details_edit),
    (r'^(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/'
        'comments$', course_comments_post),

    (r'^(?P<uni_name>[^/]+)/actions/addcourse$', add_course_view),

	(r'^(?P<uni_name>[^/]+)/$', main_page),
	(r'^$', main_page),
)
