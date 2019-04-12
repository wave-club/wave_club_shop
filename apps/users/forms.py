from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):

    username = forms.CharField(required=True, min_length = 6, max_length = 40)
    password = forms.CharField(required=True, min_length = 6, max_length = 40)
    email = forms.CharField(required=True, min_length = 6, max_length = 60)
    code = forms.CharField(required=True, min_length = 6, max_length = 20)
    captcha = CaptchaField()

