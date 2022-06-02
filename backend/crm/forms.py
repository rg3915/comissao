from django import forms

from .models import Customer, Employee


class EmployeeForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Employee
        fields = ('user', 'occupation', 'rg', 'cpf')


class CustomerForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone')
