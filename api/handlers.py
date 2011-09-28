from piston.handler import BaseHandler
from core.models import *

class UniversityHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = University

	def read(self, request, uni_id=None):
		base = University.objects
		if uni_id:
			return base.get(pk=uni_id)
		else:
			return base.all()

class UserProfileHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = UserProfile

	def read(self, request, profile_id=None):
		if profile_id:
			return UserProfile.objects.get(pk=profile_id)
		return None

class CourseHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = Course
	exclude = ('university', 'id')

	def read(self, request, course_id):
		course = Course.objects.get(pk=course_id)
		return course

class ScheduleHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = Schedule
	fields = ('university', 'creationDate', 'name', 'classes')
	
	def read(self, request, schedule_id):
		schedule = Schedule.objects.get(pk=schedule_id)

		enrollments = Enrollment.objects.filter(schedule=schedule)
		classes = []
		for enrollment in enrollments:
			section = enrollment.section.to_dict()
			classes.append(section)

		schedule.classes = classes
		return schedule

