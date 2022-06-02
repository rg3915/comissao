from django import forms

from .models import ComissionNote


class ComissionNoteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = ComissionNote
        fields = ('created_by', 'employee', 'payment_date', 'paid', 'active')

    def __init__(self, *args, **kwargs):
        super(ComissionNoteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
