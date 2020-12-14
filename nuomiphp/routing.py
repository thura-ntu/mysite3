from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^account/home', consumers.NotificationConsumer),
    url(r'^fund/(?P<fund>[\w-]+)', consumers.NotificationConsumer),
    url(r'^websockets', consumers.StreamConsumer),
]