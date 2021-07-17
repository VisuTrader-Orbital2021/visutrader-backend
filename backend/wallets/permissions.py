from wallets.models import Wallet
from rest_framework import permissions

class IsWalletOwner(permissions.BasePermission):
    """
    Custom permission to only allow owner to make CRUD operations.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

class IsHistoryOwner(permissions.BasePermission):
    """
    Custom permission to only allow history's owner to make CRUD operations.
    """
    
    def has_permission(self, request, view):
        return request.user == Wallet.objects.get(pk=view.kwargs['pk']).owner

class IsTransactionDoer(permissions.BasePermission):
    """
    Custom permission to only transaction doer to make CRUD operations.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.from_wallet.owner

class IsSuperuser(permissions.BasePermission):
    """
    Custom permission that superuser have all access to make CRUD operations.
    """
    
    def has_permission(self, request, view):
        return request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser