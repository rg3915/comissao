from django import forms

from .models import Order, Service


class ServiceForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Service
        fields = ('description', 'price', 'comission')


class OrderForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Order
        fields = ('customer', 'payment_type', 'paid', 'value')
