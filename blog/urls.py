from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(), name = 'blog-index'),
    path('<int:pk>/details',views.DetailView.as_view(), name = 'blog-post-details')
]