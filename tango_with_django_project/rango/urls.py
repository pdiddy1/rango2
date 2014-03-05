#creates django machinery to create URL mappings
from django.conf.urls import patterns, url
from rango import views

#this tuple is needed to pickup the URL mappings
#first one (^$) matches an empty string. Any URL supplied by the user that 
#matches this pattern means that the views.index() would be invoked by Django
urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^about/', views.about, name='about')
		)