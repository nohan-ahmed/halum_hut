from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views # 👈 COD view

router = DefaultRouter()
router.register('shipping-address', views.ShippingAddressViewSet, basename='shipping-address')


urlpatterns = [
    path('create-cod/', views.CreateOrderWithCOD.as_view(), name='create-cod-order'),  # 👈 COD endpoint
    path('', views.OrderList.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderUpdateDetail.as_view(), name='order-detail'),
    path('', include(router.urls)),
    
]
