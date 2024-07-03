from posts.models import Comment, Group, Post
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer,
                          GroupSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().retrieve(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post_id=self.kwargs['post_id'])

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().retrieve(request, *args, **kwargs)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
