from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

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

class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update-user.html'
    fields = ['name', 'email', 'avatar']
    success_url = reverse_lazy('accounts:myAccount')


    def get_object(self):
        return self.request.user

class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update-password.html'
    success_url = reverse_lazy('accounts:myAccount')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


updateUser = UpdateUserView.as_view()
addUser = RegisterView.as_view()
myAccount = MyAccountView.as_view()
updatePassword = UpdatePasswordView.as_view()
