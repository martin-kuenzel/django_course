"""django_project URL Configuration
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls') ),
    path('blog/', include('blog.urls') ),
    path('', include('blog.urls') ),
    path('admin/', admin.site.urls),
]
