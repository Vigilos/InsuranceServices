from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField()
    message = models.TextField(max_length=500)
