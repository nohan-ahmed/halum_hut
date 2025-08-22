from django.contrib import admin
from .models import Review, ReviewImage
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id' ,'user', 'product', 'rating', 'created_at', 'updated_at']
    list_filter = ['rating']
    search_fields = ['user__username', 'product__name']
    
    
@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_at']