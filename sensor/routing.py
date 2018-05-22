'''
Created on May 18, 2018

@author: benjamin
'''
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import sensorApp.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            sensorApp.routing.websocket_urlpatterns
        )
    ),
    })