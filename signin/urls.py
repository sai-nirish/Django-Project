from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import password_reset
from signin import views

urlpatterns = patterns('',
    url(r'^$', views.user_login),
    url(r'^index/$', views.user_login),
    url(r'^register/$', views.register),
    url(r'^logout/$',views.user_logout)
)
