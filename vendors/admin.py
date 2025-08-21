from django.contrib import admin
from .models import SellerAccount

# Register your models here.

@admin.register(SellerAccount)
class SellerAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'store_name', 'is_active', 'created_at')
    search_fields = ('user__username', 'store_name')
    list_filter = ('created_at', 'updated_at', 'is_active')