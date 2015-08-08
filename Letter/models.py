from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

# Create your models here.
class Letter(models.Model):
    recipient = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField('Date created', auto_now_add=True)
    date_received = models.DateTimeField('Deliver on:')
    privacy = models.BooleanField('Private')
    author = models.ForeignKey(User)
    sent = models.BooleanField(null=False, blank=True)

    def __str__(self):
         return self.subject






