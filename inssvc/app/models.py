from django.db import models
from django.core import validators


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=200, name='name')
    email_address = models.EmailField('Email', name='email_address')
    phone = models.CharField('Phone', max_length=20, name='phone')
    workers_comp = models.BooleanField('WorkersComp', name='workers_comp')
    general_liability = models.BooleanField(
        'GeneralLiability', name='general_liability')
    message = models.TextField('Message', max_length=500, name='message')
