from django.contrib import admin

from wallets.models import Wallet, Transaction, Position

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Position)