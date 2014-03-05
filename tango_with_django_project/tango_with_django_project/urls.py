from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	#mapping below looks for url strings that matches the patterns ^rango/
	#when a match is made, the remainder of the url string is then passed 
	#onto and handled by rango.urls
    url(r'^rango/', include('rango.urls')),
)
