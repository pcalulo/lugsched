from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render_to_response('auth/register.html', RequestContext(request, {'form': form, }))

def user_login(request):
    # If the user is logged in...
    if request.user.is_authenticated():
        # ...and the request has a 'next' parameter, redirect to that.
        # otherwise, redirect to /schedules/
        dest_url = request.GET.get('next', '/schedules/')
        return redirect(dest_url)
    
    return login(request, template_name='auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')
