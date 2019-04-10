from django import forms

class GoodsForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
