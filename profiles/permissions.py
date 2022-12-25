from rest_framework import permissions


class IsUserProfileOwnerOrReadOnly(permissions.BasePermission):
    """Allow users to modify own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to modify own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id
