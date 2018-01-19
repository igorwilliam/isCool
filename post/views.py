from django.shortcuts import render

from django.http import HttpResponse

from post.models import Topic, Reply

from post.forms import TopicForm, ReplyForm

from core.views import index

# Create your views here.
def newTopic(request):

    sucess = False
    form = TopicForm(request.POST or None)
    if form.is_valid:
        form.save()
        sucess = True
    else:
        print(form.errors)

    return HttpResponse(index(request,sucess))

def newReply(request):

    sucess = False
    form = ReplyForm(request.POST or None)
    if form.is_valid:
        form.save()
        sucess = True
    else:
        print(form.errors)

    return HttpResponse(index(request,sucess))
