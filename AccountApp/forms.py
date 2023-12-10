from django import forms
from django.forms import fields
from .models import AccountModel
from django.contrib.auth.models import User


class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        exclude = ('user',)


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        