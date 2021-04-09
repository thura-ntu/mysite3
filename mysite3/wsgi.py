"""
WSGI config for mysite3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import os
# import eventlet
import socketio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite3.settings')

application = get_wsgi_application()
# sio = socketio.Server()
# application = socketio.WSGIApp(sio, application)


from myapp import sio
import socketio

application = socketio.WSGIApp(sio, application)

import eventlet
import eventlet.wsgi

eventlet.wsgi.server(eventlet.listen(('', 8000)), application)
