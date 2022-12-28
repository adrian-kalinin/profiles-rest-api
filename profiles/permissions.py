from rest_framework import permissions


class IsUserProfileOwnerOrReadOnly(permissions.BasePermission):
    """Allow users to modify own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to modify own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id


class IsProfileFeedItemOwnerOrReadOnly(permissions.BasePermission):
    """Allow users to modify own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to modify own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.user_profile.id
