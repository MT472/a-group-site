from .models import account
from django import forms

class accountForm(forms.ModelForm):
    class Meta:
        model=account
        fields=['name','email','password','password2']