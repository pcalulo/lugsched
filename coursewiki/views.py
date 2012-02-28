# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from core.models import Course

def main_page(request):
    template = loader.get_template('coursewiki/mainpage.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def search(request):
    template = loader.get_template('coursewiki/search.html')

    results = []
    for i in range(0, 2):
        course = Course()
        course.code = 'BALIWAN'
        course.name = 'Introduction to Insanity'
        course.description = 'An in-depth blah blah blah something'
        results.append(course)

    context = RequestContext(request, {
        'searchQuery': request.GET.get('searchQuery', ''),
        'searchResults': results,
    })
    
    return HttpResponse(template.render(context))

