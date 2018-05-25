'''
Created on May 18, 2018

@author: benjamin
'''
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .topics import ALLOWED_TOPICS

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
        type_of_message = text_data_json['type']
        message = text_data_json['message']

        # sort out messages that come from browser and forward them to
        # ROS if legal        
        print(message)
        
        # Send message to channel layer
        if type_of_message == "subscribe_to_topic":
            pass
#         async_to_sync(self.channel_layer.group_send)(
#             self.group_name,
#             {
#                 'type': 'sensor_message',
#                 'message': message
#             }
#         )
    
    def sensor_message(self, event):
        message = event['message']
        # send to websocket connected to webpage
        self.send(text_data=json.dumps({
            'message': message
            }))
    
    def subscribe_to_topic(self, event):
        topic = event['message']
        if topic in ALLOWED_TOPICS:
            print('subscribe to topic ...')