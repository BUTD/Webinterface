'''
Created on May 27, 2018

@author: benjamin
'''

import websocket
from . import ros_bridge_json as rbj
import json

class RosWebsocketApp(websocket.WebSocketApp):
    '''
    classdocs
    '''
    
    def __init__(self, url, consumer):
        super().__init__(url)
        self.debugHelper = False
        self.consumer = consumer
        websocket.enableTrace(True)


    def on_data(self, message, data_type, do_continue):
        print("Hello from on_data()")
    
    def on_message(self, message_json):
        # is called on incoming message from ROS's websocket
        print("Received message from ROS...")
        message_dict = rbj.get_message_from_json(message_json)
        message = message_dict.get("msg").get("data")
        print(message)
        # send to web page
        self.cosumer.send(text_data=json.dumps({
            'message': message
            }))
        
    def on_error(self, error):
        print("There was an error:")
        print(error)
        
    def on_open(self):
        print("Opened web socket...")
        
    def on_close(self):
        print("Closing web socket...")