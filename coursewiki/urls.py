from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from piston.resource import Resource
from views import *

urlpatterns = patterns('',
    # e.g. /uni/De La Salle University/actions/search
    (r'^uni/(?P<uni_name>[^/]+)/actions/search$', search_view),

    # e.g. /uni/De La Salle University/courses/BASICON/
    (r'^uni/(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/$', course_details_view),
    (r'^uni/(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/edit$',
        course_details_edit),
    (r'^uni/(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/comments$',
        course_comments_post),

    # e.g. /wiki/uni/De La Salle University/courses/BASICON
    (r'^uni/(?P<uni_name>[^/]+)/courses/(?P<course_code>[^/]+)/$', course_details_view),


    (r'^uni/(?P<uni_name>[^/]+)/actions/addcourse$', add_course_view),

    # e.g. /wiki/uni/De La Salle University/
	(r'^uni/(?P<uni_name>[^/]+)/$', main_page),
	(r'^$', main_page),
)
