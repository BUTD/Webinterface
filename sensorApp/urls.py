'''
Created on May 18, 2018

@author: benjamin
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sensor/$', views.sensor),
    url(r'drive/$', views.drive),
    url(r'status/motors/$', views.motors)
    ]