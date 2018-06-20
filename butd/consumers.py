'''
Created on May 18, 2018

@author: benjamin
'''
#from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer 
import json
from .topics import ALLOWED_TOPICS_READ, ALLOWED_TOPICS_WRITE

import websocket
from . import ros_bridge_json as rbj
import threading

class SensorConsumer(WebsocketConsumer):
    def connect(self):
        # accept connection
        self.accept()
        # gruppe einstellen auf "sensorGroup"
#         self.group_name = 'sensorGroup'
#         async_to_sync(self.channel_layer.group_add)(
#             self.group_name,
#             self.channel_name)
        # open websocket at start
        def on_message(ws, message_json):
            # is called on incoming message from ROS's websocket
            # print("Received message from ROS...")
            message_dict = rbj.get_message_from_json(message_json)
            # message = message_dict.get("msg").get("data")
            message = message_dict.get("msg")
            topic = message_dict.get("topic")
            # print(message_dict.get("topic"))
            # send to web page
            self.send(text_data=json.dumps({
                'message': message,
                'topic': topic,
                }))
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
        print("Connection to ROS websocket established.")
    
    def disconnect(self, code):
        self.ros_websocket.close()
        print("Connection to ROS websocket closed.")
    
    def receive(self, text_data):
        # this function is called on incoming messages from web page
        print("Received!!" + text_data)
        text_data_json = json.loads(text_data)
        type_of_message = text_data_json['type']
        message = text_data_json['message']

        # sort out messages that come from browser and forward them to
        # ROS if allowed
        
        # Send message to ROS's websocket
        # subscribe to ROS topic
        if type_of_message == "subscribe_to_topic":
            if message in ALLOWED_TOPICS_READ:
                print("Topic allowed!")
                self.ros_websocket.send(rbj.get_json_subscribe(message))
            else:
                print("Topic " + message + " not allowed!")
        # unscubscribe from ROS topic
        elif type_of_message == "unsubscribe_from_topic":
            if message in ALLOWED_TOPICS_READ:
                self.ros_websocket.send(rbj.get_json_unsubscribe(message))
        # publish message to topic
        elif type_of_message == "publish_to_topic":
            topic = text_data_json['topic']
            if topic in ALLOWED_TOPICS_WRITE:
                self.ros_websocket.send(rbj.get_json_publish_string(topic, message))
                