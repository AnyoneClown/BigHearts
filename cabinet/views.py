from rest_framework import generics
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated

from cabinet.models import Post
from cabinet.serializers import PostSerializer


class PostView(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser]

    def perform_update(self, serializer):
        serializer.save(status="New")
