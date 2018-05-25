'''
Created on May 18, 2018

@author: benjamin
'''
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, SyncConsumer 
import json
from .topics import ALLOWED_TOPICS

import websocket
from . import ros_bridge_json as rbj
import threading

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
        print(type_of_message)
        
        # Send message to channel layer
        if type_of_message == "subscribe_to_topic":
            print("OK")
            async_to_sync(self.channel_layer.send)(
                'request_to_ROS',
                {'type': 'subscribe_to_ROS_topic', 'message':message}
                )
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
            
class WebsocketTunnelConsumer(SyncConsumer):
    ros_websocket = 0
    wst = 0
    
    def init_ROS_websocket(self, event):
        if not self.ros_websocket:
            # open websocket at first start
            def on_message(ws, message_json):
                message_dict = rbj.get_message_from_json(message_json)
                message = message_dict.get("msg").get("data")
                async_to_sync(self.channel_layer.group_send)(
                    'sensorGroup',
                    {'type': 'sensor_message', 'message': message}
                )
            def on_error(ws, error):
                print("There was an error:")
                print(error)
            def on_open(ws):
                print("Opened web socket...")
            def on_close(ws):
                print("Closing web socket...")
            self.ros_websocket =  websocket.WebSocketApp(
                "ws://localhost:9090",
                on_message = on_message,
                on_error = on_error,
                on_close = on_close,
                on_open = on_open
            )
            # from https://stackoverflow.com/questions/29145442/threaded-non-blocking-websocket-client
            self.wst = threading.Thread(target=self.ros_websocket.run_forever)
            self.wst.daemon = True
            self.wst.start()
    
    def stop_ROS_websocket(self, event):
        pass        
    
    def subscribe_to_ROS_topic(self, event):
        print("function subscribe_to_ROS_topic")
        print(event)
        topic = event['message']
        self.ros_websocket.send(rbj.get_json_subscribe(topic))
        

        