from django.shortcuts import render
from .models import Post

# Create your views here.
def index(req):
    context = {
        'title': 'Blog`s',
        'posts': Post.objects.all()
    }
    return render(req,'blog/index.html',context)