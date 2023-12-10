from django import forms
from django.db import models
from django.db.models import fields
from .models import Category, Product


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        
        
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('slug',)
        


