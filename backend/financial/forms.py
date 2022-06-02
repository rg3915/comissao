from django import forms

from .models import ComissionNote


class ComissionNoteForm(forms.ModelForm):
    required_css_class = 'required'

    payment_date = forms.DateField(
        label='Data de pagamento',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = ComissionNote
        fields = ('created_by', 'employee', 'payment_date', 'paid')
