"""django_project URL Configuration
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('polls/', include('polls.urls') ),
    path('blog/', include('blog.urls') ),
    path('', include('polls.urls') ),
    
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),

    path('registration/', include('registration.urls')),
    
    # path('', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
