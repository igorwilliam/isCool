from django.urls import path

from . import views

app_name = 'material'
urlpatterns = [
    path('adicionar-material/', views.addMaterial, name='addMaterial'),
    path('listar-materiais/', views.listMaterial, name='listMaterial'),
    path('listar-materiais/', views.listMaterial, name='listMaterial'),
    path('editar-material/(?P<id>[0-9]+)/', views.editMaterial, name="editMaterial"),


]
