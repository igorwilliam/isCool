from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from post.models import Topic, Reply

from post.forms import TopicForm, ReplyForm

from core.views import index

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def newTopic(request):

    form = TopicForm(request.POST or None)
    if form.is_valid:
        form.save()
        sucess = True
    else:
        print(form.errors)

    return redirect('index')

@login_required
def newReply(request):

    form = ReplyForm(request.POST or None)
    if form.is_valid:
        form.save()
        sucess = True
    else:
        print(form.errors)

    return redirect('index')

    # return HttpResponse(index(request,sucess))

class editTopicView(object):

    def __call__(self, request, id):

        topic = get_object_or_404(Topic, id=id)
        if request.method == 'POST':
            form = TopicForm(data=request.POST, instance=topic)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = TopicForm(instance=topic)

        context = {
            'form': form,
        }

        return render(request, 'post/edit-topic.html', context)

editTopic = editTopicView()

class editReplyView(object):

    def __call__(self, request, id):

        reply = get_object_or_404(Reply, id=id)
        if request.method == 'POST':
            form = ReplyForm(data=request.POST, instance=reply)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ReplyForm(instance=reply)

        context = {
            'form': form,
        }

        return render(request, 'post/edit-reply.html', context)

editReply = editReplyView()

def deleteTopic(request, id):
    topic = Topic.objects.get(id=id).delete()
    return redirect('index')

def deleteReply(request, id):
    reply = Reply.objects.get(id=id).delete()
    return redirect('index')
