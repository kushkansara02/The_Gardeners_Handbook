from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import WishList


#from .models import User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name'
        ]

class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = [
            'flowers'
        ]