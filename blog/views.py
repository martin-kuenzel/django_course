from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post

