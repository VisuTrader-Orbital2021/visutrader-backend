from rest_framework import permissions

class IsUser(permissions.BasePermission):
    """
    Custom permission that it is the user
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj

class IsSuperuser(permissions.BasePermission):
    """
    Custom permission that superuser have all access to make CRUD operations.
    """
    
    def has_permission(self, request, view):
        return request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser