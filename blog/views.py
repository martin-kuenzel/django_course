from django.shortcuts import render

# Create your views here.
def index(req):
    context = {
        'title': 'Mainsite'
    }
    return render(req,'blog/index.html',context)