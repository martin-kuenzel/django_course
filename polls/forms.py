from django.forms import ModelForm
from .models import Poll, OptionSet
from extra_views import InlineFormSetFactory

class OptionSetInLineFormSet(InlineFormSetFactory):
    model = OptionSet
    exclude = ['delete']
    factor_kwargs = {
        'extra' : 1
    }
    # fields = ['title']

class PollCreateForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['title','content']
