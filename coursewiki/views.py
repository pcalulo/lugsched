# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

def main_page(request):
	template = loader.get_template('coursewiki/mainpage.html')
	context = RequestContext(request, {
		'cake': False,
    })
	return HttpResponse(template.render(context))

