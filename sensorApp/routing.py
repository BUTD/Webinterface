'''
Created on May 18, 2018

@author: benjamin
'''
from django.conf.urls import url
from sensorApp import consumers

websocket_urlpatterns = [
    url(r'^ws/sensor/$', consumers.SensorConsumer),
    ]