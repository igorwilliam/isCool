from django.shortcuts import render
from django.http import HttpResponse

from post.models import Topic, Reply

# Create your views here.

def index(request):
    context = {
        'topics': Topic.objects.all(),
        'replies': Reply.objects.all()
    }
    return render(request, 'index.html', context)
