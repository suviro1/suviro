from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the form widgets
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({
        'class': 'form-control',
        'type': 'number',
        'inputmode': 'numeric',
        'pattern': '[0-9]*',
        'name': 'phone'
})

        self.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 4})
