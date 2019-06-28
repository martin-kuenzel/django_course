from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

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
    try:
        selected_option = poll.option_set.get(pk=req.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render('polls/poll_details.html',{
            'poll_id': poll.pk,
            'error_msg':"Your selected choice was invalid."
        })
    else:
        selected_option.votes += 1
        selected_option.save()
    
    return HttpResponseRedirect( reverse( 'poll-results', args=(poll.pk,) ) )