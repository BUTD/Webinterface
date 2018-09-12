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

def get_json_publish_stop_message(topic):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {}
        })
def get_json_publish_stop_follow_message(topic):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {}
        })
    
def get_json_publish_demo_message(topic):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {"data": 1}
        })
    
def get_json_publish_follow_message(topic):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {"data": 2}
        })
    
def get_json_publish_reset_message(topic):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {"data": 0}
        })
def get_json_publish_stop_demo_message(topic):
    return json.dumps({
        "op": "publish",
        "topic": topic,
        "msg": {}
        })

def get_message_from_json(message_json):
    message_dict = json.loads(message_json)
    return message_dict