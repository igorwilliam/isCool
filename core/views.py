from django.shortcuts import render
from django.http import HttpResponse


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

class IndexView(object):

    def __call__(self, request, sucess=False ):

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

index = IndexView() #criando view em forma de classes

def erro404(request):

    return render(request,'404.html')
