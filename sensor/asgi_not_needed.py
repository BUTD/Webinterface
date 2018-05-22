'''
Created on May 18, 2018

@author: benjamin
'''
import os
import channels.layers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensor.settings")
channel_layer = channels.layers.get_channel_layer() 