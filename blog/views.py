from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts_total_list = Post.objects.all() # db SELECT * FROM POST
    
    return render(request, 
                  template_name='blog/index.html',
                  context={'posts':posts_total_list},
                  )
    
def detail(request, pk):
    posts_page_list = Post.objects.get(pk=pk)
    
    return render(request,
                  template_name='blog/detail.html',
                  context={'post_page' : posts_page_list})