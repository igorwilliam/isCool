from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('novo-usuario/', views.addUser, name='addUser'),
    path('minha-conta/', views.myAccount, name='myAccount'),
]
