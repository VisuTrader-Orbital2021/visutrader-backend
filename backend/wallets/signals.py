from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from wallets.models import Wallet, Transaction, Position

INITIAL_AMOUNT = 100_000

@receiver(post_save, sender=get_user_model(), dispatch_uid='wallets.signals.create_wallet')
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(balance=INITIAL_AMOUNT, owner=instance)

@receiver(post_save, sender=get_user_model(), dispatch_uid='wallets.signals.create_position')
def create_position(sender, instance, created, **kwargs):
    if created:
        Position.objects.create(owner=instance, data={})

@receiver(post_save, sender=Transaction, dispatch_uid='wallets.signals.update_wallet')
def update_wallet(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.get(pk=instance.from_wallet.pk)
        
        if instance.transaction_type == "buy":
            wallet.balance = wallet.balance - instance.amount
        else:
            wallet.balance = wallet.balance + instance.amount

        wallet.save()

@receiver(post_save, sender=Transaction, dispatch_uid='wallets.signals.update_position')
def update_position(sender, instance, created, **kwargs):
    if created:
        position = Position.objects.get(pk=instance.from_wallet.owner.position.pk)

        if instance.transaction_type == "buy":
            if not (instance.market in position.data.keys()):
                position.data[instance.market] = 0
            position.data[instance.market] += instance.quantity

        elif instance.transaction_type == "sell":
            position.data[instance.market] -= instance.quantity
        
        position.save()