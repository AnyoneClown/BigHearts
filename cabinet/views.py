from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cabinet.models import Post
from cabinet.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
