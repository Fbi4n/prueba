from django.forms import ModelForm
from .models import Task
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese Titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripcion'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'}),
        }