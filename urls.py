from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'lugsched.views.home', name='home'),
	# url(r'^lugsched/', include('lugsched.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

    (r'accounts/', include('lugsched.auth.urls')),
	(r'^api/', include('lugsched.api.urls')),
	(r'^schedules/', include('lugsched.schedules.urls')),
	(r'^coursewiki/', include('lugsched.coursewiki.urls')),
	(r'^$', include('lugsched.appbase.urls')),

    # Redirect requests for /favicon.ico to its true location
    # See http://www.codekoala.com/blog/2008/setup-faviconico-django/
    (r'^favicon\.ico', 'django.views.generic.simple.redirect_to', 
        {'url': '/static/images/favicon.ico'}),
)
