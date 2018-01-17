from django import forms

from .models import Topic, Reply

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
