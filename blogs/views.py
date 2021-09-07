from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer
from .models import Blog
# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    ## Give it the main query for the index route
    queryset = Blog.objects.all()
    # THe serializer for serializing
    serializer_class = BlogSerializer
    ## Optional Permissions
    permission_classes = [permissions.AllowAny]