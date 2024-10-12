from django import forms

class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

