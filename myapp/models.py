from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict
# from django.db.models import signals
# import socketio
# import asyncio
import socketio
sio = socketio.AsyncServer(async_mode='asgi')


class Device(models.Model):
    address = models.CharField('device logical address', max_length=255, unique=True)


@receiver(post_save, sender=Device)
def notify_new_device_created(instance, created, **kwargs):
    print("Post save 1 emited for", instance)
    data = model_to_dict(instance, ['id', 'address'])
    sio.emit('new_device', data=data)


# def create_badge(sender, instance, created, **kwargs):
#     print("Post save 2 emited for", instance)
#     data = model_to_dict(instance, ['id', 'address'])
#     sio.emit('new_device', data=data)
#
#
# signals.post_save.connect(create_badge, sender=Device)