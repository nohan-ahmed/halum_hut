from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('shipping-address', views.ShippingAddressViewSet, basename='shipping-address')


urlpatterns = [
    path('create-cod/', views.CreateOrderWithCOD.as_view(), name='create-cod-order'),
    path('create-stripe-order/', views.CreateOrderWithStripe.as_view(), name='create-stripe-order'),
    path('stripe-webhook/', views.stripe_webhook_view, name='stripe-webhook'),
    path('', views.OrderList.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderUpdateDetail.as_view(), name='order-detail'),
    path('', include(router.urls)),
]
