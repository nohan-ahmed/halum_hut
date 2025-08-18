from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from notifications.tasks import send_notification_task

@receiver(post_save, sender=Order)
def notify_new_order(sender, instance, created, **kwargs):
    if created:
        send_notification_task.delay(
            recipient=instance.user,
            title=f'{instance.status} Order',
            message=f"Your order has been {instance.status}. Order ID: {instance.pk}",
            notification_type='order',
        )
        
        pass
        
    else:
        send_notification_task.delay(
            recipient=instance.user,
            title=f'{instance.status} Order',
            message=f"Your order has been {instance.status}. Order ID: {instance.pk}",
            notification_type='order',
        )
        