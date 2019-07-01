from django.shortcuts import render, render_to_response

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from django.views import generic

from .form import PostCreateForm
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post

class PostCreateView(generic.edit.FormView):
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm

@login_required
def save_post(req):
    user = req.user
    if req.method == 'POST':
        post = Post(author=user,title=req.POST['title'],content=req.POST['content'])
        # if form.is_valid:
        post = post.save()
        return HttpResponseRedirect( reverse( 'blog_index') )

        # return render_to_response('blog_index',RequestContext(req))
