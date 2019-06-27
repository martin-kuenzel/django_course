from django.shortcuts import render
from .models import Poll

# Create your views here.
def index(req):
    context = {
        'title': 'Polls',
        'polls': Poll.objects.all()
    }
    return render(req,'polls/index.html',context)

def poll_details(req,id):
    context = {
        'poll': Poll.objects.get(id=id)
    }
    return render(req,'polls/poll_details.html',context)