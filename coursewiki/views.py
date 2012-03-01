# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.http import urlquote_plus, urlquote
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from core.models import *

@login_required
def main_page(request, uni_name=None):
    if not uni_name:
        profile = request.user.get_profile()
        uni_name = profile.university.name
        return redirect('/coursewiki/' + urlquote(uni_name, safe='') + '/')


    template = loader.get_template('coursewiki/mainpage.html')
    context = RequestContext(request, {
        'uni_name': uni_name,
    })
    return HttpResponse(template.render(context))

def search(request):
    template = loader.get_template('coursewiki/search.html')
    uni = University.objects.get(pk=1)

    results = []
    for i in range(0, 2):
        course = Course()
        course.code = 'BALIWAN'
        course.name = 'Introduction to Insanity'
        course.description = 'An in-depth blah blah blah something'
        course.university = uni
        results.append(course)

    context = RequestContext(request, {
        'searchQuery': request.GET.get('searchQuery', ''),
        'searchResults': results,
    })
    
    return HttpResponse(template.render(context))

