from piston.handler import BaseHandler
from core.models import University

class UniversityHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = University

	def read(self, request, uni_id=None):
		base = University.objects
		if uni_id:
			return base.get(pk=uni_id)
		else:
			return base.all()

