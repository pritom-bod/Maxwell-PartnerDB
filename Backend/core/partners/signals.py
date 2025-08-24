import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Partner
from .serializers import PartnerSerializer

def broadcast(action, instance: Partner):
    channel_layer = get_channel_layer()
    payload = {
        "action": action,  # "create" | "update" | "delete"
        "partner": PartnerSerializer(instance).data if instance else None,
        "id": instance.id if instance else None,
    }
    async_to_sync(channel_layer.group_send)(
        "partners",
        {"type": "partner_event", "payload": payload}
    )

@receiver(post_save, sender=Partner)
def on_save(sender, instance, created, **kwargs):
    broadcast("create" if created else "update", instance)

@receiver(post_delete, sender=Partner)
def on_delete(sender, instance, **kwargs):
    broadcast("delete", instance)
