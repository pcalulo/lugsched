# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

def hello(request):
	template = loader.get_template('appbase/home.html')
	context = RequestContext(request, {
		'cake': False,
	})
	return HttpResponse(template.render(context))

