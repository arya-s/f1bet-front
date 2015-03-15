from django.conf.urls import patterns, url

from f1betapi import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)