from django.db import models


class ContactUs(models.Model):
    name = models.CharField('Your Name', max_length=200, name='name')
    email_address = models.EmailField('Email', name='email_address')
    message = models.TextField('Message', max_length=500, name='message')
