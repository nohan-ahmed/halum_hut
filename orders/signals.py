from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItem
from notifications.tasks import send_notification_task


"""
Sends a notification to the user when an order is created or updated.
"""
@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        send_notification_task.delay(
            recipient_id=instance.user.id,
            title=f'{instance.status} Order',
            message=f"Your order has been {instance.status}. Order ID: {instance.pk}",
            notification_type='order',
        )
        
        pass
        
    else:        
        send_notification_task.delay(
            recipient_id=instance.user.id,
            title=f'{instance.status} Order',
            message=f"Your order has been {instance.status}. Order ID: {instance.pk}",
            notification_type='order',
        )
        
        
        
"""
Sends a notification to the product owner when a new order item is created.
"""    
@receiver(post_save, sender=OrderItem)
def send_order_item_notification(sender, instance, created, **kwargs):
    if created:
        rechipient_user = instance.product_variant.product.seller.user
        send_notification_task.delay(
            recipient_id=rechipient_user.id,
            title=f'A new order has been placed. Order ID: {instance.order.pk}',
            message=f"Product: {instance.product_variant.product.name} - Quantity: {instance.quantity} - Subtotal: {instance.subtotal}",
            notification_type='order',
        )
              