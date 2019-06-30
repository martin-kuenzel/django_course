from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(), name = 'blog_index'),
    path('<int:pk>/details/',views.DetailView.as_view(), name = 'post_details'),

    path('post_create/',views.PostCreateView.as_view(), name = 'post_create'),
    path('post_create_done/', views.save_post, name = 'post_create_done')
]