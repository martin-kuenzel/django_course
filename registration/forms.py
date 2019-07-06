from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=75,help_text='required field')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
