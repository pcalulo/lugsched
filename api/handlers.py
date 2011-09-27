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
