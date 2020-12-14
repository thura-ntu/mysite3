from django.db import models

# Create your models here.
class ThreadTask(models.Model):
    pass


from django.db import models
from django.forms.models import model_to_dict
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from django.core.serializers.json import DjangoJSONEncoder
from asgiref.sync import async_to_sync
import json

class DeribitFundingData(models.Model):
    time = models.DateTimeField()
    rate = models.FloatField()

    def __str__(self):
        return str(self.time)

def save_post(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = model_to_dict(instance)
    json_data = json.dumps(data, cls=DjangoJSONEncoder)
    async_to_sync(channel_layer.group_send)(
        "echo_group",
        {"type": "stream", "data": json_data},
    )

post_save.connect(save_post, sender=DeribitFundingData)