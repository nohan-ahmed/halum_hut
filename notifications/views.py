from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import F
from .models import Notification
from .serializers import NotificationSerializer
from core.paginations import StandardResultsSetPagination


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        # Optimize query if recipient is a ForeignKey
        return Notification.objects.filter(recipient=self.request.user).select_related('recipient').order_by('-created_at')

    @action(detail=False, methods=['get'])
    def unread(self, request):
        unread = self.get_queryset().filter(is_read=False)
        page = self.paginate_queryset(unread)
        if page is not None:
            serializer = NotificationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = NotificationSerializer(unread, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        notification = self.get_object()
        if notification.is_read:
            return Response({'detail': 'Already marked as read.'}, status=status.HTTP_200_OK)
        notification.is_read = True
        notification.save(update_fields=['is_read'])
        return Response(NotificationSerializer(notification).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def mark_all_read(self, request):
        updated = self.get_queryset().filter(is_read=False).update(is_read=True)
        return Response({'marked_as_read': updated}, status=status.HTTP_200_OK)
