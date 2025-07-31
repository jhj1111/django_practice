"""
URL configuration for django_project_practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_project_practice import settings
# http://127.0.0.1:8000/


# url -> ~/patterns 로 보냄
# ex) http://127.0.01:8000/admin -> ...
# path("blog/", admin.site.urls), -> http://127.0.01:8000/blog -> ...
# http://127.0.01:8000/blog -> ...


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('single_pages.urls')),
    path('blog/', include('blog.urls')),
    path('library/', include('library.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)