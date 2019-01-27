from django.http import JsonResponse
from .models import Blogs
from .serializers import BlogsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework import status
# Create your views here.

class BlogsClass(ListAPIView):
    serializer_class = BlogsSerializer
    '''
    Get all blogs
    '''
    def get(self, request, *args, **kwargs):
        blogs = Blogs.objects.all();
        if blogs:
            bdata = BlogsSerializer(blogs, many=True)
            return Response({'status_code':200,'message':'SUCCESS','data':bdata.data})

    '''
    Save a blog
    '''
    def post(self, request, *args, **kwargs):
        if request.data:
            blog_data = request.data
        else:
            return Response({'status_code':200,'message':'FAILURE', 'errors': 'no data posted'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BlogsSerializer(data=blog_data, context={'request': request})
        if serializer.is_valid():
            blog = serializer.save()
            if blog:
                return Response({'status_code':200,'message':'SUCCESS', 'blog': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': 0, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
