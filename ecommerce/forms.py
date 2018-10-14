from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Properties
from ecommerce.choices import *


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact = forms.IntegerField(label='Contact', required=True)
    type = forms.ChoiceField(choices=USER_TYPE_CHOICES, initial='', widget=forms.Select(), label='User Type',
                             required=True)
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



class PropertyPostForm(forms.ModelForm):
    property_title = forms.CharField(label='Post Title', required=True)
    locality = forms.CharField(label='Locality', required=True)
    property_type = forms.ChoiceField(choices=PROPERTY_TYPE_CHOICES, widget=forms.Select(), label='Property Type',
                                      required=True)
    price = forms.IntegerField(label='Price', required=True)
    BHK = forms.ChoiceField(choices=BHK_CHOICES, widget=forms.Select(), label='BHK', required=False)
    construction_status = forms.ChoiceField(choices=CONSTRUCTION_STATUS_CHOICES, widget=forms.Select(),
                                            label='Construction Status', required=True)
    area = forms.CharField(label="Area", required=True)
    address = forms.CharField(widget=forms.Textarea(), label='Address', required=True)
    description = forms.CharField(widget=forms.Textarea(), label='Description', required=False)

    class Meta:
        model = Properties
        fields = (
            'property_title', 'locality', 'property_type', 'price', 'BHK', 'construction_status', 'area',
            'address', 'description'
        )
