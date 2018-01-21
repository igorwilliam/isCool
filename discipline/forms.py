from django import forms

from .models import Discipline,RegisterStudent

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = RegisterStudent
        fields = '__all__'
