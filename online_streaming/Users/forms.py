from django import forms

class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterUser(forms.Form):
    email = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data =  super().clean()
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 and password2 and password1 == password2:
            return data
        
        else:
            return forms.ValidationError('No good')