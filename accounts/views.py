from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserAdminCreationForm
# Create your views here.

class RegisterView(CreateView):

    model = User
    template_name = "accounts/add_user.html"
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

class MyAccountView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/minha-conta.html"

addUser = RegisterView.as_view()
myAccount = MyAccountView.as_view()
