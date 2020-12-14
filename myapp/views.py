from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


# import eventlet
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
