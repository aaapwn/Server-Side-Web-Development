from django.forms import ModelForm
from .models import Employee, Project
from company.models import Position
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

class EmployeeForm(ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={"cols": 30, "rows": 3}))
    district = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=15)
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta:
        model = Employee
        fields = [
            "first_name", 
            "last_name", 
            "gender", 
            "birth_date", 
            "hire_date", 
            "salary", 
            "position",
            "location",
            "district",
            "province",
            "postal_code"
        ]
        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)
        if cleaned_data.get('hire_date') > timezone.localtime().date():
            raise ValidationError("Hire date cannot be in the future.")
        if cleaned_data.get('position'):
            cleaned_data['position_id'] = cleaned_data.get('position').id
            # print(cleaned_data)
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
