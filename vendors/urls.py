from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'seller-account', views.SellerAccountView, basename='seller-account')


urlpatterns = [
    path('', include(router.urls)),
]