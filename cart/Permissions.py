from rest_framework import permissions

class IsOwnerForCartItem(permissions.BasePermission):
    """
    Allows access only to the owner of the CartItem's cart.
    """

    def has_permission(self, request, view):
        # Allow access only if user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow only if the cart's owner is the requesting user
        return obj.cart.user == request.user
