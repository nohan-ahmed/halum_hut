import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from .models import Notification
from .serializers import NotificationSerializer

logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Called when a websocket connection is opened.
        Authenticates user and adds to their private notification group.
        """
        self.user = self.scope.get("user")
        if self.user is None or isinstance(self.user, AnonymousUser):
            await self.close()
            return

        self.group_name = f"user_{self.user.id}_notifications"

        try:
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()
            # Send unread notifications on connect
            unread_notifications = await self.get_unread_notifications()
            await self.send(text_data=json.dumps({
                "type": "unread_notifications",
                "notifications": unread_notifications,
                "unread_count": len(unread_notifications),
            }))
        except Exception as e:
            logger.exception(f"Error connecting WebSocket for user {self.user.id}: {e}")
            await self.close()

    async def disconnect(self, close_code):
        """
        Called when websocket disconnects.
        Removes the user from their notification group.
        """
        if hasattr(self, "group_name"):
            try:
                await self.channel_layer.group_discard(self.group_name, self.channel_name)
            except Exception as e:
                logger.exception(f"Error disconnecting WebSocket for user {self.user.id}: {e}")

    async def receive(self, text_data):
        """
        Called when a message is received from the frontend.
        Supports actions: mark_read, mark_all_read
        """
        try:
            data = json.loads(text_data)
            action = data.get("action")

            if action == "mark_read":
                notif_id = data.get("id")
                if notif_id:
                    await self.mark_as_read(notif_id)

            elif action == "mark_all_read":
                await self.mark_all_as_read()

            else:
                logger.warning(f"Unknown action received: {action}")

        except json.JSONDecodeError:
            logger.warning("Invalid JSON received in WebSocket.")
        except Exception as e:
            logger.exception(f"Error processing WebSocket message: {e}")

    async def send_notification(self, event):
        """
        Sends a single notification to the frontend.
        Triggered by `group_send` in the backend.
        """
        try:
            notification_data = event.get("notification")
            if notification_data:
                await self.send(text_data=json.dumps({
                    "type": "notification",
                    "notification": notification_data
                }))
        except Exception as e:
            logger.exception(f"Error sending notification to user {self.user.id}: {e}")

    # ------------------------------
    # Database helper methods
    # ------------------------------
    @database_sync_to_async
    def mark_as_read(self, notif_id):
        Notification.objects.filter(id=notif_id, recipient=self.user).update(is_read=True)

    @database_sync_to_async
    def mark_all_as_read(self):
        Notification.objects.filter(recipient=self.user, is_read=False).update(is_read=True)

    @database_sync_to_async
    def get_unread_notifications(self):
        notifications = Notification.objects.filter(recipient=self.user, is_read=False).order_by("-created_at")
        return NotificationSerializer(notifications, many=True).data
