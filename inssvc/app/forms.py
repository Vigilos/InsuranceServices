from django import forms
from django.forms import ModelForm
from .models import ContactUs


class EmailForm(ModelForm):
    name = forms.TextInput(attrs={'class': 'form_name', 'id': 'name_id'})
    email_address = forms.EmailField()
    message = forms.TextInput()

    class Meta:
        model = ContactUs
        fields = ['name', 'email_address', 'message']
        labels = {}
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form_name', 'id': 'name_id'}),
        #     'email_address': forms.EmailInput(),
        #     'message': forms.TextInput(),
        # }
