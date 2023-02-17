from django.db import models
from django.core import validators


class ContactUs(models.Model):
    name = models.CharField('Your Name', max_length=200, name='name')
    email_address = models.EmailField('Email', name='email_address', error_messages={
                                      'invalid': 'Please enter a correct email address'
                                      })
    message = models.TextField('Message', max_length=500, name='message')
