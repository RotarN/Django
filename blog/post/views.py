from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


# Create your views here.


def apostlist(request):
    postlist = Post.objects.all()
    return render(request, template_name='postlist.html', context={'posts': postlist})


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#    permission_classes = [permissions.AllowAny]


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
#    permission_classes = [permissions.AllowAny]