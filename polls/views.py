from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import PollCreateForm
from .models import Poll, Option

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    """ get all polls whose date_created lies before/on now """
    def get_queryset(self):
        return Poll.objects.filter( date_created__lte = timezone.now() ).order_by('-date_created') #[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_details.html'

    """ get poll`s details if its date_created lies before/on now """
    def get_queryset(self):
        return Poll.objects.filter( date_created__lte = timezone.now() )
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_results.html'

    """ get poll`s details if its date_created lies before/on now """
    def get_queryset(self):
        return Poll.objects.filter( date_created__lte = timezone.now() )

def poll_vote(req,poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    selected_options = []

    # loop through the polls optionsets 
    for optionset in poll.optionset_set.all():
    
        # try to assign current optionset`s seleced option to a value
        try:
            selected_option = optionset.option_set.get( pk = req.POST[f'{optionset.pk}'] )
            #selected_option = poll.optionset_set.get(pk=req.POST['option'])

        # if the assignment throws an exception return to the poll, hence forcing the user to restart ... hehehe
        except (KeyError, Option.DoesNotExist):
            return render('polls/poll_details.html',{
                'poll_id': poll.pk,
                'error_msg':"Your selected choice was invalid."
            })

        # if the assignment is valid add the selected option to a list
        else:
            selected_options.append(selected_option)

    # All selected options are valid, hence += 1 all of them 
    for selected_option in selected_options:
        selected_option.votes += 1
        selected_option.save()

    return HttpResponseRedirect( reverse( 'poll_results', args=(poll.pk,) ) )

## Poll creation

class PollCreateView(generic.edit.FormView):
    template_name = 'polls/poll_create.html'
    form_class = PollCreateForm

@login_required
def save_poll(req):
    if req.method == 'POST':
        poll = Poll(author=req.user, title=req.POST['title'], content=req.POST['content'])
        #if poll.is_valid: #TODO
        poll.save()
        return HttpResponseRedirect( reverse( 'poll_index') )
