from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from post.models import Topic, Reply
from discipline.models import RegisterStudent, Discipline
from post.forms import TopicForm, ReplyForm



# Create your views here.
#
# def index(request, sucess=False):
#
#     form = TopicForm()
#
#     context = {
#         'topics': Topic.objects.all(),
#         'replies': Reply.objects.all(),
#         'form': form,
#         'sucess': sucess,
#     }
#     return render(request, 'index.html', context)
@login_required
def index(request, sucess=False ):

    formReply = ReplyForm()
    formTopic = TopicForm()

    context = {
        'topics': Topic.objects.all(),
        'replies': Reply.objects.all(),
        'disciplines': Discipline.objects.all(),
        'registers': RegisterStudent.objects.all(),
        'formReply': formReply,
        'formTopic': formTopic,
        'sucess': sucess,
    }

    return render(request, 'index.html', context)

def erro404(request):

    return render(request,'404.html')
