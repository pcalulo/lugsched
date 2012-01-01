# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

def sched_home(request):
	template = loader.get_template('schedules/schedules.html')
	context = RequestContext(request, {
		'cake': False,
    })
	return HttpResponse(template.render(context))

