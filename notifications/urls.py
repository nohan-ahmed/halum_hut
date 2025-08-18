from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.NotificationList.as_view(), name='notification-list'),
    
]
