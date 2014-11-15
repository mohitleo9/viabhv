from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)


class Message(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
