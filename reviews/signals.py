from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review
from notifications.tasks import send_notification_task


"""
Signal to send a notification when a review is created.
"""
@receiver(post_save, sender=Review)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        send_notification_task.delay(
            recipient_id=instance.product.seller.user.id,
            title=f'Review for {instance.product.name}',
            message=f"Your review for {instance.product.name} has been submitted. Review ID: {instance.pk}",
            notification_type='review',
        )
