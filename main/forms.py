from .models import Employee, Role, Task
from django.forms import ModelForm, TextInput
from django import forms


class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'age', 'salary', 'role']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Введите ФИО'}),
            'age': TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'Введите возраст'}),
            'salary': TextInput(attrs={'class': 'form-control',
                                       'placeholder': 'Введите зарплату'}),
        }


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['info', 'employee', 'completed']
        widgets = {
            'info': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Введите описание задачи'}),
        }


class RoleForm(ModelForm):

    class Meta:
        model = Role
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Введите название должности'}),
        }
