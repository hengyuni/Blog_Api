from .models import Blog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BlogSerializer

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  permission_classes = [permissions.AllowAny]
