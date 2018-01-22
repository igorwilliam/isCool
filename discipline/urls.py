from django.urls import path

from . import views

app_name = 'discipline'
urlpatterns = [
    path('ver-disciplinas/', views.listDiscipline, name="listDiscipline"),

    path('adicionar-disciplina/', views.addDiscipline, name="addDiscipline"),
    path('mudar-estado/(?P<id>[0-9]+)/', views.registerStudent, name="registerStudent"),
    path('editar-disciplina/(?P<id>[0-9]+)/', views.editDiscipline, name="editDiscipline"),
    path('gerenciar-alunos/', views.listStudent, name="listStudent"),
    path('gerenciar-disciplina/', views.managerDiscipline, name="managerDiscipline"),
    path('deletar-disciplina/(?P<id>[0-9]+)/', views.deleteDiscipline, name="deleteDiscipline"),

]
