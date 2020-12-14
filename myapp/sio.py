import os
import socketio
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite3.settings")
# manager = socketio.RedisManager('')
manager = socketio.RedisManager('redis://')
sio = socketio.Server(client_manager=manager)


# sio = socketio.AsyncServer(async_mode='asgi')
# app = socketio.ASGIApp(sio, static_files={
#     '/': 'index.html',
#     '/static': 'static',
# })