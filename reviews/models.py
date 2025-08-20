from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # 1 to 5 stars

    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE) # normal relationship
    product = models.ForeignKey("products.Product", related_name="reviews", on_delete=models.CASCADE) # trying to use Lazy relationship ✅
    order_item = models.ForeignKey("orders.OrderItem", on_delete=models.SET_NULL, null=True, blank=True) # trying to use Lazy relationship ✅
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=255, blank=True)
    comment = models.TextField(blank=True)
    images = models.ManyToManyField("ReviewImage", blank=True) # trying to use Lazy relationship✅
    is_verified_purchase = models.BooleanField(default=False)  # if review linked with an order
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'user')  # one user can review a product only once

    def __str__(self):
        return f"{self.product.name} - {self.rating}★ by {self.user.username}"


class ReviewImage(models.Model):
    image = models.ImageField(upload_to="reviews/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review Image {self.id}"