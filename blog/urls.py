# from django_project_practice.urls import urlpatterns
from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/blog/
    path('<int:pk>/', views.detail, name='pk'), # 127.0.0.1:8000/blog/{pk}/
    path('create/', views.create, name='create'), # 127.0.0.1:8000/blog/create/
    path('createfake/', views.createfake, name='createfake'), # 127.0.0.1:8000/blog/createfake/
    path('download/', views.file_download, name='file_download'), # 127.0.0.1:8000/blog/file_download/
    path('categories/<str:slug>/', views.categories, name='categories'), # 127.0.0.1:8000/blog/categories/{slug}/
]