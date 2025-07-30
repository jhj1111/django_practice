# from django_project_practice.urls import urlpatterns
from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/blog/
    path('<int:pk>/', views.detail, name='pk'), # 127.0.0.1:8000/blog/{pk}/
]