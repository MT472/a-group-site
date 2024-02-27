from django import forms

class SignupForm(forms.Form):
    username=forms.CharField(max_length=255)
    email=forms.EmailField()
    password=forms.CharField(max_length=255)
    password2=forms.CharField(max_length=255)
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            return forms.ValidationError('password fields do not match')
        return self.cleaned_data['password2']
        

class LoginForm(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255)
    