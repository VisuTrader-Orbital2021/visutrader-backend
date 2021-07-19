from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.
class Wallet(models.Model):
    balance = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wallets', on_delete=models.CASCADE)

class Transaction(models.Model):
    BUY = "buy"
    SELL = "sell"
    TRANSACTION_TYPE_CHOICES = [
        (BUY, "Buy"),
        (SELL, "Sell")
    ]

    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    market = models.CharField(max_length=4)
    from_wallet = models.ForeignKey(Wallet, related_name='history', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Position(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='position', on_delete=models.CASCADE)
    position = models.JSONField(blank=True)