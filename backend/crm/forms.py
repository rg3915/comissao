from django import forms

from .models import Customer, Employee


class EmployeeForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Employee
        fields = ('user', 'occupation', 'rg', 'cpf', 'active')

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomerForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone', 'active')

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
