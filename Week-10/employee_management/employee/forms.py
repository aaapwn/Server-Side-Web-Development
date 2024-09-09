from django.forms import ModelForm
from .models import Employee, Project
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('hire_date') > timezone.localtime().date():
            raise ValidationError("Hire date cannot be in the future.")
        return cleaned_data

class ProjectFrom(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('start_date') > cleaned_data.get('due_date'):
            raise ValidationError("Start date cannot be greater than due date.")
        return cleaned_data
