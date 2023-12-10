from django import forms
from .models import SellModel


class SellForm(forms.ModelForm):
    class Meta:
        model = SellModel
        exclude = ('slug',)

        widgets = {
            'sell_date': forms.DateInput(attrs={'type':'date'}),
            'sale_note': forms.Textarea(attrs={'rows': '3'}),
        }



