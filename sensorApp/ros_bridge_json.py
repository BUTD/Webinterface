'''
Functions to create JSON strings to access rosbridge web sockets
Created on Apr 25, 2018

@author: benjamin
'''
import json

def get_json_subscribe(topic):
    return json.dumps({"op": "subscribe", "topic": topic})

def get_json_unsubscribe(topic):
    return json.dumps({"op": "unsubscribe", "topic": topic})

def get_json_publish_string(topic, message):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {"data": message}})

def get_message_from_json(message_json):
    message_dict = json.loads(message_json)
    return message_dict