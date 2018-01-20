from django.urls import path

from . import views

app_name = 'discipline'
urlpatterns = [
    path('adicionar-disciplina/', views.addDiscipline, name="addDiscipline"),
    path('ver-disciplinas/', views.listDiscipline, name="listDiscipline"),
]
