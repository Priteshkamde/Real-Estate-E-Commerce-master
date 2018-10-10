from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from ecommerce.choices import *


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact = forms.IntegerField(label='Contact', required=True)
    type = forms.ChoiceField(choices=USER_TYPE_CHOICES, initial='', widget=forms.Select(), label='User Type', required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'contact', 'type')


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    contact = forms.IntegerField(label='Contact', required=True)
    type = forms.CharField(label='User Type', required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'contact', 'type')
