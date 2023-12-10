from django import forms
from .models import UserModel
from django.contrib.auth.models import User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ('user',)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)



