from django.forms import ModelForm

from .models import Poll

class PollCreateForm(ModelForm):
    class Meta:
        fields = ['title','content']
        model = Poll