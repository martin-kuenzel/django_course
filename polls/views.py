from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.views import generic
from django.contrib.auth.decorators import login_required

from extra_views import CreateWithInlinesView

from .forms import PollCreateForm, OptionSetInLineFormSet
from .models import Poll, Option, OptionSet

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    # get all polls whose date_created lies before/on now
    def get_queryset(self):
        return Poll.objects.filter( date_created__lte = timezone.now() ).order_by('-date_created') #[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_details.html'

    # get poll`s details if its date_created lies before/on now
    def get_queryset(self):
        return Poll.objects.filter( date_created__lte = timezone.now() )

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_results.html'

    # get poll`s details if its date_created lies before/on now
    def get_queryset(self):
        return Poll.objects.filter( date_created__lte = timezone.now() )

#########
def poll_vote(req,poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    selected_options = []
    if( req.method == 'POST'):

        # loop through the polls optionsets 
        for optionset in poll.optionset_set.all():

            if f'{optionset.pk}' in req.POST: 
                pk = req.POST[f'{optionset.pk}']
                selected_option = optionset.option_set.get( pk = pk )
                selected_options.append(selected_option)

        # Make all selected options, += 1 
        for selected_option in selected_options:
            selected_option.votes += 1
            selected_option.save()

        return HttpResponseRedirect( reverse( 'poll_results', args=(poll.pk,) ) )
    else:
        return HttpResponseRedirect( reverse( 'poll_details', args=(poll.pk,) ) )


## Poll creation
    
#############
class PollCreateView(CreateWithInlinesView):
    model = Poll
    inlines = [OptionSetInLineFormSet]
    template_name = 'polls/poll_create.html'
    form_class = PollCreateForm


### THIS DOES NOT SAVE ANYTHING BECAUSE IT'S USELESS TO DO SO
@login_required
def save_poll(req):
    if req.method == 'POST':
        poll = Poll(author=req.user, title=req.POST['title'], content=req.POST['content'])
        print(req.POST.__str__())
        #if poll.is_valid: #TODO
        #poll.save()
        return HttpResponseRedirect( reverse( 'poll_index') )
