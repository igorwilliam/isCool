from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('novo-topico/', views.newTopic, name="newTopic"),
    path('nova-resposta/', views.newReply, name="newReply"),
    path('editar-topico/(?P<id>[0-9]+)/', views.editTopic, name="editTopic"),
    path('editar-comentario/(?P<id>[0-9]+)/', views.editReply, name="editReply"),
    path('deletar-topico/(?P<id>[0-9]+)/', views.deleteTopic, name="deleteTopic"),
    path('deletar-comentario/(?P<id>[0-9]+)/', views.deleteReply, name="deleteReply"),

]
