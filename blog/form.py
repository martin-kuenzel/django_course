from django.forms import ModelForm

from .models import Post

class PostCreateForm(ModelForm):
    class Meta:
        fields = ['title','content']
        model = Post
