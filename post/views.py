from django.shortcuts import render

from django.http import HttpResponse

from post.models import Topic, Reply

from post.forms import TopicForm, ReplyForm

# Create your views here.
def newTopic(request):

    form = TopicForm(request.POST or None)
    if form.is_valid:
        form.save()
        return render(request, 'index.html')
    else:
        print(form.errors)


    return render(request, 'index.html')
