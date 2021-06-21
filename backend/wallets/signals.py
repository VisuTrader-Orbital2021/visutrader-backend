from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from wallets.models import Wallet, Transaction

@receiver(post_save, sender=get_user_model(), dispatch_uid='wallets.signals.create_wallet')
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(balance=100000, owner=instance)

@receiver(post_save, sender=Transaction, dispatch_uid='wallets.signals.update_wallet')
def update_wallet(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.get(pk=instance.from_wallet.pk)
        wallet.balance = wallet.balance + instance.amount
        assert wallet.balance >= 0
        wallet.save()