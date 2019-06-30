from django import forms
from django.contrib.auth.models import User
from .models import Sub, Custom

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class CustomForm(forms.ModelForm):
    class Meta:
        model = Custom
        fields =['sub', 'period','price','last_pay']