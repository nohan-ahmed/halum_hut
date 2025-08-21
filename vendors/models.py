from django.db import models
from accounts.models import User
# Create your models here.
class SellerAccount(models.Model):
    """
    Model to store seller account information.
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='seller_account')
    store_name = models.CharField(max_length=100)
    store_description = models.TextField(blank=True)
    store_logo = models.ImageField(upload_to='store_logos/', blank=True, null=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Available for payout
    pending_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Recently earned but not yet withdrawable
    total_earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name