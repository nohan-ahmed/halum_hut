from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from core.Permissions import IsOwnerOrReadOnly
from core.paginations import StandardResultsSetPagination
from .models import Review
from .serializers import ReviewSerializer
from products.models import Product


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    GET → list all reviews for a product
    POST → create a review for a product
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        product_id = self.kwargs.get("product_id")
        return Review.objects.filter(product_id=product_id).order_by("-created_at")

    def perform_create(self, serializer):
        product_id = self.kwargs.get("product_id")
        # Note: get_object_or_404 will raise a 404 error if the object is not found
        product = get_object_or_404(Product, pk=product_id)

        # Prevent multiple reviews from same user
        if Review.objects.filter(product=product, user=self.request.user).exists():
            raise ValidationError({"detail": "You have already reviewed this product."})

        serializer.save(product=product, user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET → single review details
    PUT/PATCH → update review (only owner)
    DELETE → delete review (only owner)
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise ValidationError("You can only edit your own reviews.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise ValidationError("You can only delete your own reviews.")
        instance.delete()
