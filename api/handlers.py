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

class UniversityCourseHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('id', 'code', 'name', 'description')
	model = Course

	def read(self, request, uni_id, course_id=None):
		if course_id:
			if not isinstance(course_id, int):
				return Course.objects.get(university__pk=uni_id, code=course_id)
			else:
				course = Course.objects.get(pk=course_id)
		else:
			return Course.objects.filter(university__pk=uni_id)
		return None

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

	def read(self, request, course_id=None, uni_id=None):
		if course_id:
			return Course.objects.get(pk=course_id)
		elif uni_id:
			return Course.objects.filter(university__pk=uni_id)
		return None

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

