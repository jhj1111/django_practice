from django.shortcuts import render
from django.shortcuts import redirect   # 주소 변경
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from blog.models import *

from .utils.serializers import *

import os

# Create your views here.
@api_view(['GET'])    
def helloAPI(request):
    return Response('hello world rest reponse')

@api_view(['GET', 'POST'])
def blogAPI(request):
    if request.method=='GET':
        posts = Post.objects.all()
        post_serializer = PostSeializer(posts, many=True)   # Serialize
        return Response(post_serializer.data, status=HTTP_200_OK)
    
    else :  # POST, json -> post로 변환
        de_serializer = PostSeializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            
            return Response(de_serializer.data, status=HTTP_201_CREATED)
        
    return Response(de_serializer.data, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def postAPI(request, pk):
    post = get_object_or_404(klass=Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    
    if request.method=='GET':
        post_serializet = PostSeializer(post)   # Serialize
        return Response(post_serializet.data, status=HTTP_200_OK)
    elif request.method=='DELETE':
        post.delete()
        return Response('delete completed', status=HTTP_204_NO_CONTENT)
    else :
        seializer = PostSeializer(post, data=request.data)
        if seializer.is_valid():
            seializer.save()
            return Response(seializer.data, status=HTTP_200_OK)
            
    return Response(seializer.errors, status=HTTP_400_BAD_REQUEST)
        

def example(request):
    
    return render(request, 
                  template_name='rest_example/example.html',
                  context={
                            }
                  )
    
@api_view(['GET', 'POST'])
def commentAPI(request, pk):
    if request.method=='GET':
        comment = Comment.objects.get(pk=pk)
        comment_serializer = CommentSeializer(comment, many=True)   # Serialize
        return Response(comment_serializer.data, status=HTTP_200_OK)
    
    else :  # POST, json -> post로 변환
        de_serializer = CommentSeializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            
            return Response(de_serializer.data, status=HTTP_201_CREATED)
        
    return Response(de_serializer, status=HTTP_400_BAD_REQUEST)
