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
    path('<int:pk>/delete/', views.delete, name='delete'), # 127.0.0.1:8000/blog/{pk}/delete/
    path('<int:pk>/update/', views.create, name='update'), # 127.0.0.1:8000/blog/{pk}/update/
    path('<int:pk>/comment_create/', views.comment_create, name='comment_create'), # 127.0.0.1:8000/blog/{pk}/commnet_input/
    path('<int:pk>/comment_delete/<int:id>/', views.comment_delete, name='comment_delete'), # 127.0.0.1:8000/blog/{pk}/commnet_delete/
    path('<int:pk>/comment_update/<int:id>/', views.comment_create, name='comment_update'), # 127.0.0.1:8000/blog/{pk}/commnet_delete/
]