from django.contrib.auth import get_user_model
from rest_framework import serializers

from cabinet.models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault()
    )
    status = serializers.CharField(default="New")
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "type",
            "title",
            "category",
            "text",
            "image",
            "phone_number",
            "telegram",
            "location",
            "status",
            "services",
            "delivery",
            "person",
            "link",
            "url"
        ]

    def get_url(self, obj):
        return obj.url
