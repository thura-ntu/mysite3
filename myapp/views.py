from django.shortcuts import render
from .models import Device
from datetime import datetime


# Create your views here.
def index(request):
    obj_device = Device()
    obj_device.address = "asdfsadf - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    obj_device.save()
    return render(request, 'index.html')

import eventlet
#
# async_mode = eventlet
# import os
# from django.http import HttpResponse
# import socketio
#
# basedir = os.path.dirname(os.path.realpath(__file__))
# sio = socketio.Server(async_mode='eventlet')
#
#
# @sio.on('connection-bind')
# def connection_bind(sid, data):
#     print("sid:", sid, "data", data)
#
#
# @sio.on('message')
# def message(data):
#     print(data)
#     sio.emit('test', data)
#
#
# @sio.on('disconnect')
# def test_disconnect(sid):
#     print("Disconnected")
#
#
# def hello(data):
#     return HttpResponse("Hello")
