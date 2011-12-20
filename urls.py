from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'falone.views.home', name='home'),
	# url(r'^falone/', include('falone.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	(r'^api/', include('falone.api.urls')),
	(r'^$', include('falone.appbase.urls')),

    # Redirect requests for /favicon.ico to its true location
    # See http://www.codekoala.com/blog/2008/setup-faviconico-django/
    (r'^favicon\.ico', 'django.views.generic.simple.redirect_to', 
        {'url': '/static/images/favicon.ico'}),
)
