from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.managers import AccountManager

# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    display_name = models.CharField('Display Name', max_length=225)
    username = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'display_name']

    objects = AccountManager()

    def __str__(self):
        return self.email
    
    # TODO: check whether we need to add permissions or not