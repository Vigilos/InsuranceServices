from django import forms
from django.forms import ModelForm
from .models import ContactUs


class EmailForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_name form-control', 'id': 'name_id'}))
    email_address = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ex. you@domain.com'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ex. (555) 555-5555'}))
    workers_comp = forms.BooleanField(required=False)
    general_liability = forms.BooleanField(required=False)
    message = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Tell us how we can help you', 'rows': '5'}))

    class Meta:
        model = ContactUs
        fields = ['name', 'email_address', 'phone', 'message']
        labels = {}
