from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(), name = 'blog-index'),
    path('<int:pk>/details/',views.DetailView.as_view(), name = 'blog-post-details'),

    path('post-create/',views.PostCreateView.as_view(), name = 'blog-post-create'),
    path('post-create-done/', views.save_post, name = 'blog-post-create-done')
]