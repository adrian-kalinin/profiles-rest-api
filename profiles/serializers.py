from rest_framework import serializers

from profiles import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

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
