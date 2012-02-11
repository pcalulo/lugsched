# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect

def home_page(request):
	# If the user is logged in, redirect them to the schedules page.
	if request.user.is_authenticated():
		return redirect('/schedules/')

	# Otherwise, present them the home page
	template = loader.get_template('appbase/home.html')
	context = RequestContext(request, {
		'cake': False,
	})
	return HttpResponse(template.render(context))

