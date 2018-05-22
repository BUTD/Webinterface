'''
Created on May 18, 2018

@author: benjamin
'''
from django.core.management import BaseCommand

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
# import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        channel_layer = get_channel_layer()
        x=1
        while True:
            async_to_sync(channel_layer.group_send)(
                'sensorGroup',
                {'type': 'sensor_message', 'message': str(x)}
            )
            time.sleep(1)
            x+=1
            self.stdout.write("Sensor reading..." + str(x))
            
            # Hier könnte auch Code stehen, der mit einem externen
            # websocket oder direkt mit ROS kommuniziert