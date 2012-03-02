# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.http import urlquote_plus, urlquote
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from datetime import datetime

from core.models import *

def get_most_recent_courses():
    # The most recently created course will be the first one listed
    return Course.objects.order_by('-creation_date')[:5]

@login_required
def main_page(request, uni_name=None):
    if not uni_name:
        profile = request.user.get_profile()
        uni_name = profile.university.name
        return redirect('/coursewiki/' + urlquote(uni_name, safe='') + '/')

    if uni_name == 'actions':
        return HttpResponseNotFound()

    template = loader.get_template('coursewiki/mainpage.html')
    context = RequestContext(request, {
        'uni_name': uni_name,
        'recent_courses': get_most_recent_courses()
    })
    return HttpResponse(template.render(context))

def search_view(request, uni_name=None):
    template = loader.get_template('coursewiki/search.html')

    results = Course.objects.all()

    context = RequestContext(request, {
        'searchQuery': request.GET.get('searchQuery', ''),
        'searchResults': results,
    })
    
    return HttpResponse(template.render(context))

def add_course_on_post(request, uni_name=None):
    try:
        profile = request.user.get_profile()
    except Exception:
        return HttpResponseForbidden()

    university = profile.university

    course = Course()
    course.code = request.POST.get('courseCode')
    course.name = request.POST.get('courseName')
    course.description = request.POST.get('description', '')
    course.university = university
    course.creation_date = datetime.now()

    course.save()
    return redirect('/coursewiki/')
    

def add_course_view(request, uni_name=None):
    if request.method == 'POST':
        return add_course_on_post(request)

    context = RequestContext(request)
    template = loader.get_template('coursewiki/addcourse.html')
    return HttpResponse(template.render(context))

