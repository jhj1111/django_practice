from rest_framework import serializers
from blog.models import *

# class CategorySeializet(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['name', 'slug']
        
class PostSeializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'category', 'author', 'create_date', 'updated_date', 'content', 'uploaded_image', 'uploaded_file']
        # fields = ['__all__']
        
class CommentSeializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'created_date', 'updated_date']
        