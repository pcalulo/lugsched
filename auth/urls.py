from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'register/$', register, name='register'),
    # url(r'login/$', login, {'template_name': 'auth/login.html'}),
    url(r'login/$', user_login),

    # It *might* be more likely that when a user logs out, he's simply letting
    # a friend log in.
    # TODO: Double-check this guess regarding logouts
    url(r'logout/$', user_logout)
)

