'''
Created on May 18, 2018

@author: benjamin
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sensor/$', views.sensor, name='sensor'),
    url(r'drive/$', views.drive, name='drive'),
    url(r'status/motors/$', views.motors, name='motors'),
    url(r'test/$', views.test, name='test'),
    ]