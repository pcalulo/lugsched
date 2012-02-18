from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import *

uni_handler = Resource(UniversityHandler)
uni_course_handler = Resource(UniversityCourseHandler)
profile_handler = Resource(UserProfileHandler)
course_handler = Resource(CourseHandler)
section_handler = Resource(SectionHandler)
schedule_handler = Resource(ScheduleHandler)

urlpatterns = patterns('',
	# University
	(r'^university/(?P<uni_id>[^/]+)/courses/(?P<course_id>[^/]+)', uni_course_handler),
	(r'^university/(?P<uni_id>[^/]+)/courses/', uni_course_handler),
	(r'^university/(?P<uni_id>[^/]+)/', uni_handler),
	(r'^university/', uni_handler),

	# UserProfile
	(r'^profile/(?P<profile_id>[^/]+)/', profile_handler),
	(r'^profile/', profile_handler),

    # Sections
	(r'^course/(?P<course_id>[^/]+)/section/(?P<section_id>[^/]+)', section_handler),
	(r'^course/(?P<course_id>[^/]+)/section/', section_handler),
	(r'^section/(?P<section_id>)[^/]+', section_handler),
	(r'^section/', section_handler),

	# Course
	(r'^course/(?P<course_id>[^/]+)/', course_handler),
	(r'^course/', course_handler),

	# Schedule
	(r'^schedule/', schedule_handler),
	(r'^schedule/(?P<schedule_id>[^/]+)/', schedule_handler),
)
