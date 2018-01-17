from django.shortcuts import render
from django.http import HttpResponse

from post.models import Topic, Reply

from post.forms import TopicForm, ReplyForm

# Create your views here.

def index(request):

    form = TopicForm()

    context = {
        'topics': Topic.objects.all(),
        'replies': Reply.objects.all(),
        'form': form,
    }
    return render(request, 'index.html', context)

def newTopic(request):

    form = TopicForm(request.POST or None)
    if form.is_valid:
        form.save()
        return HttpResponse('Tarefa adicionada com sucesso !!!')
    else:
        print(form.errors)


    return render(request, 'index.html')
