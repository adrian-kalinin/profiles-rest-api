from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings

from profiles import models, permissions, serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsUserProfileOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("email", "name")


class UserLoginApiView(ObtainAuthToken):
    """Create user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handle profile feed items"""

    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsProfileFeedItemOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        """Set user profile to logged in user"""
        serializer.save(user_profile=self.request.user)
