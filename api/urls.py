from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import *

uni_handler = Resource(UniversityHandler)
profile_handler = Resource(UserProfileHandler)
course_handler = Resource(CourseHandler)

urlpatterns = patterns('',
	# University
	(r'^university/(?P<uni_id>[^/]+)/', uni_handler),
	(r'^university/', uni_handler),

	# UserProfile
	(r'^profile/(?P<profile_id>[^/]+)/', profile_handler),
	(r'^profile/', profile_handler),

	# Course
	(r'^course/(?P<course_id>[^/]+)/', course_handler),
)
