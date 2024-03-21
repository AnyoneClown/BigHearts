from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from cabinet.models import Post
from cabinet.serializers import (
    PostSerializer,
    PostListSerializer,
    AdminSerializer,
    FilterPostsSerializer,
)


class PostView(generics.CreateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser]

    def perform_update(self, serializer):
        if "status" not in serializer.validated_data:
            serializer.save(status="New")
        else:
            serializer.save(status=serializer.validated_data["status"])

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostListSerializer
        return self.serializer_class


class UserPost(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class AdminView(generics.ListAPIView):
    queryset = Post.objects.filter(status="New")
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class FilterPosts(APIView):

    def post(self, request):
        serializer = FilterPostsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            post_type = serializer.validated_data["type"]
            category = serializer.validated_data.get("category")

            if category is None:
                posts = Post.objects.filter(type=post_type, status="Active")
            else:
                posts = Post.objects.filter(type=post_type, category=category, status="Active")

            data = [
                {
                    "title": post.title,
                    "image": post.image,
                    "location": post.location,
                    "url": post.url,
                }
                for post in posts
            ]
            return Response(data, status=status.HTTP_200_OK)
