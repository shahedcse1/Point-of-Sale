from django import forms
from django.db import models
from .models import CustomerModel


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        exclude = ('slug',)

        
