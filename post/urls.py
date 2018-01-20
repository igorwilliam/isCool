from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('novo-topico/', views.newTopic, name="newTopic"),
    path('nova-resposta/', views.newReply, name="newReply"),
]
