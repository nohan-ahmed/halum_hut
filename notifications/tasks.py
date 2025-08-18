from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from accounts.models import User
from .models import Notification
from .serializers import NotificationSerializer
import time


@shared_task
def send_notification_task(recipient, title, message, notification_type='message', sender_id=None, url=None):
    sender = User.objects.get(id=sender_id) if sender_id else None
    
    # Create the notification instance
    notification = Notification.objects.create(recipient=recipient, sender=sender, title=title, message=message, notification_type=notification_type, url=url)
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{recipient.id}_notifications",
        {
            "type": "send_notification",
            "notification": NotificationSerializer(notification).data,
        }
    )
    
    # Send the notification to the recipient    
    return notification.id
