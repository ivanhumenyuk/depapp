from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'department_id',
            'hire_date'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'hire_date': forms.TextInput(attrs={'class': 'form-control'})
        }