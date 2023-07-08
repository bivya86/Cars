from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        model=User
        fields=['username','password' ,'email']
        widgets={'password':forms.PasswordInput()}
        help_texts = {'username' : ''}

class CarForm(forms.ModelForm):
    class Meta():
        model = Cars
        fields = '__all__'