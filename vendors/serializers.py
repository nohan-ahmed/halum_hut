from rest_framework import serializers
from .models import SellerAccount
class SellerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerAccount
        fields = ('id', 'user', 'store_name', 'store_description', "store_logo", "contact_email", "contact_phone", "balance", "pending_balance", "total_earnings", "is_active", 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', "balance", "pending_balance", "total_earnings", "is_active", 'created_at', 'updated_at')