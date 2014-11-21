from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views

urlpatterns = patterns('',
	url('^check/$', views.checkcourse),
	url('^$', views.index),
	url('^fill/$', views.fill),
	url(r'^verify/$',views.verify),
	url(r'^lock/$', views.lock),
	)
