# from django_project_practice.urls import urlpatterns
from django.urls import path    
from . import views

urlpatterns = [
    path('', views.example, name='example'), # 127.0.0.1:8000/example/
    path('helloAPI/', views.helloAPI, name='helloAPI'), # 127.0.0.1:8000/example/helloAPI
    path('blogAPI/', views.blogAPI, name='blogAPI'), # 127.0.0.1:8000/example/getAPI
    path('postAPI/<int:pk>/', views.postAPI, name='postAPI'), # 127.0.0.1:8000/example/postAPI
    path('commentAPI/<int:pk>/', views.commentAPI, name='commentAPI'), # 127.0.0.1:8000/example/postAPI
]