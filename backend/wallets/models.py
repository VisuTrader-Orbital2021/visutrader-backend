from django.db import models
from django.conf import settings

# Create your models here.
class Wallet(models.Model):
    balance = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wallets', on_delete=models.CASCADE)

class Transaction(models.Model):
    amount = models.IntegerField()
    market = models.CharField(max_length=4)
    from_wallet = models.ForeignKey(Wallet, related_name='history', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
