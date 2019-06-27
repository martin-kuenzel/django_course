from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Poll, Option

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Poll.objects.order_by('-date_created') #[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_details.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_results.html'

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