from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser

class UserCreationForm(UserCreationForm):
    email = EmailField(max_length=75)

    class Meta:
        model = SiteUser
        fields = ('username','email','password1','password2')
