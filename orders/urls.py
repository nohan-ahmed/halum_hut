from django.urls import path
from . import views  # 👈 COD view


urlpatterns = [
    path('create-cod/', views.CreateOrderWithCOD.as_view(), name='create-cod-order'),  # 👈 COD endpoint
    path('', views.OrderList.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderUpdateDetail.as_view(), name='order-detail'),
    
]
