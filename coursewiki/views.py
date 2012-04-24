from django.http import *
from django.template import RequestContext, loader

# String sanitization
from django.utils.http import urlquote_plus, urlquote

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Required data for comments
from django.contrib.sites.models import Site

# The preview view must be exempt from CSRF protection
from django.views.decorators.csrf import csrf_exempt

import markdown
from datetime import datetime

from core.models import *

def get_newest_courses():
    # The most recently created course will be the first one listed
    return Course.objects.order_by('-creation_date')[:5]

# Prepare our markdown object
# For information on the parameters, see:
# http://packages.python.org/Markdown/reference.html
md = markdown.Markdown(safe_mode='escape')


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
        'newest_courses': get_newest_courses()
    })
    return HttpResponse(template.render(context))

@login_required
def search_view(request, uni_name):
    template = loader.get_template('coursewiki/search.html')

    results = Course.objects.all()

    context = RequestContext(request, {
        'uni_name': uni_name,
        'searchQuery': request.GET.get('searchQuery', ''),
        'searchResults': results,
    })
    
    return HttpResponse(template.render(context))

def course_details_view(request, uni_name, course_code):
    template = loader.get_template('coursewiki/coursedetails.html')

    course = Course.objects.get(code = course_code)

    context = RequestContext(request, {
        'course': course,
        'sections': Section.objects.filter(course = course),
    })

    return HttpResponse(template.render(context))

def course_comments_post(request, uni_name, course_code):
    # Accept only POSTs for now
    if request.method != 'POST':
        # TODO implement other HTTP methods
        return HttpResponseBadRequest('<h1>HTTP 400 Bad Request</h1>')

    # Make sure the course exists
    try:
        course = Course.objects.get(code = course_code)
    except DoesNotExist:
        return HttpResponseNotFound()

    comment_text = request.readlines()
    comment = Comment()
    comment.content_object = course
    comment.site = Site.objects.get_current()
    comment.user = request.user
    comment.comment = comment_text
    comment.ip_address = request.META['REMOTE_ADDR']
    comment.is_public = True
    comment.is_removed = False
    comment.save()

@csrf_exempt
def course_comments_preview(request, uni_name, course_code):
    # Only accept POST requests
    if request.method != 'POST':
        return HttpResponseBadRequest('<h1>HTTP 400 Bad Request</h1>')
    
    comment_text = str(request.body)

    print 'REQUEST BODY: ', comment_text

    md.reset()
    markdowned_text = md.convert(comment_text)

    return HttpResponse(markdowned_text)
    

@login_required
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
    course.creator = request.user
    course.creation_date = datetime.now()

    course.save()

    # Redirect to the newly-created course
    return redirect('/coursewiki/%s/courses/%s' %
        (urlquote(university.name, safe=''), urlquote(course.code, safe=''))
    )
    
@login_required
def add_course_view(request, uni_name=None):
    if request.method == 'POST':
        return add_course_on_post(request)

    context = RequestContext(request)
    template = loader.get_template('coursewiki/addcourse.html')
    return HttpResponse(template.render(context))

