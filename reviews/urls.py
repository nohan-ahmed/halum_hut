from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path("products/<int:product_id>/", ReviewListCreateView.as_view(), name="product-reviews"),
    path("<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]
