'''
Created on May 18, 2018

@author: benjamin
'''
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class SensorConsumer(WebsocketConsumer):
    def connect(self):
        # gruppe einstellen auf "sensorGroup"
        self.group_name = 'sensorGroup'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name)
        # Verbindung akzeptieren
        self.accept()
    
    def disconnect(self, code):
        pass
    
    def receive(self, text_data):
        print("Received!!" + text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'sensor_message',
                'message': message
            }
        )
    
    def sensor_message(self, event):
        message = event['message']
        # send to websocket
        self.send(text_data=json.dumps({
            'message': message
            }))