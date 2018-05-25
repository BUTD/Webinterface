'''
Created on May 19, 2018

@author: benjamin
'''
from django.core.management import BaseCommand

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# import time
import websocket
from . import ros_bridge_json as rbj
try:
    import thread
except ImportError:
    import _thread as thread
# import json

topic = "/hc04"
channel_layer = get_channel_layer()

def on_message(ws, message_json):
    message_dict = rbj.get_message_from_json(message_json)
    print(message_dict)
    message = message_dict.get("msg").get("data")
    print(message)
    # forward message to Django Channel layer
    # filters could be applied here
    # messages come from sensorApp.consumers
    async_to_sync(channel_layer.group_send)(
        'sensorGroup',
        {'type': 'sensor_message', 'message': message}
    )
    
    
def on_error(ws, error):
    print("There was an error:")
    print(error)
    
def on_open(ws):
    print("Opened web socket...")
    def run(*args):
        print('Subscribing to topic "%s"' % (topic))
        ws.send(rbj.get_json_subscribe(topic))
    thread.start_new_thread(run, ())

def on_close(ws):
    print("Closing web socket...")
    

class Command(BaseCommand):
    def handle(self, *args, **options):
        ws = websocket.WebSocketApp("ws://localhost:9090",
                                    on_message = on_message,
                                    on_error = on_error,
                                    on_close = on_close,
                                    on_open = on_open)

        ws.run_forever()