from django import forms

from .models import Discipline

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'
