from django import forms
from django.contrib.auth.models import User
class SignupForm(forms.Form):
    username=forms.CharField(max_length=255)
    email=forms.EmailField()
    image=forms.ImageField()
    phone=forms.IntegerField()
    work=forms.CharField(max_length=250)
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(widget=forms.PasswordInput)
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']