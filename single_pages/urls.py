# from django_project_practice.urls import urlpatterns
from django.urls import path    
from . import urls  # sigle_pages의 urls
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about')
]