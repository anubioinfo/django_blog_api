from rest_framework import serializers
from .models import Blogs


class BlogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogs
        fields = ('id', 'title', 'content', 'author', 'create_date', 'update_date')