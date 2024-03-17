import requests
from django.contrib.auth import get_user_model
from rest_framework import serializers

from cabinet.models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault()
    )
    status = serializers.CharField(default="New")
    image_file = serializers.ImageField(allow_null=True, required=False, write_only=True)

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
            "email",
            "image_file",
            "url"
        ]

    def create(self, validated_data):
        image_file = validated_data.pop("image_file", None)
        if image_file:
            imgbb_api_url = "https://api.imgbb.com/1/upload?key=9239b8d19c1953b12e55807bf850c584"
            response = requests.post(imgbb_api_url, files={"image": image_file})
            if response.status_code == 200:
                image_data = response.json()["data"]
                image_url = image_data["url"]
                validated_data["image"] = image_url
        return super().create(validated_data)


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "user",
            "type",
            "title",
            "category",
            "text",
            "phone_number",
            "telegram",
            "location",
            "status",
            "services",
            "delivery",
            "person",
            "link",
            "image",
            "email",
            "url",
        ]

    def get_url(self, obj):
        return obj.url
