from django import forms

from .models import Order, Service


class ServiceForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Service
        fields = ('description', 'price', 'comission')

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Order
        fields = ('customer', 'payment_type', 'paid', 'value')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
