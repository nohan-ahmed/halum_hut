from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

# Local imports
from .serializers import SellerAccountSerializer
from .models import SellerAccount
from core.Permissions import IsOwnerOrReadOnly
from core.paginations import StandardResultsSetPagination

# Create your views here.
class SellerAccountView(ModelViewSet):
    queryset = SellerAccount.objects.all()
    serializer_class = SellerAccountSerializer
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['id', 'store_name', 'store_description']
    filterset_fields = ["user", 'store_name']
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Ensure that the user does not already have a seller account
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError({"error": "User already has a seller account."})
    
