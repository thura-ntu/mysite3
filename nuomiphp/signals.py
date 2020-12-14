from django.db.models.signals import pre_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer
from .models import ThreadTask



@receiver(pre_save, sender=ThreadTask)
def notify_thread_task_save(sender, **kwargs):
    if "instance" in kwargs:
        instance = kwargs["instance"]
        # check if there is a new notification
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "task", {"type": "user_notification",
                     "event": "New Notification",
                     "notification": instance.text}
        )
