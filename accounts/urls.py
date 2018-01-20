from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('novo-usuario/', views.addUser, name='addUser'),
    path('minha-conta/', views.myAccount, name='myAccount'),
    path('atualizar-dados/', views.updateUser, name='updateUser'),
    path('atualizar-senha/', views.updatePassword, name='updatePassword'),

]
