from rest_framework import serializers

from profiles import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes user profiles"""

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            password=validated_data.get("password"),
        )

        return user

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ("id", "user_profile", "status_text", "created")
        extra_kwargs = {"user_profile": {"read_only": True}}
