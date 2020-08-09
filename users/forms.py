from django import forms
from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate


class createUserForm():
    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name'
                'username',
                'password1',
                'password2',
                'ethnicity',
                'gender',
                'age',
                'email',
                'education',
                'disability',
                ]

def __str__(self):
    return f"{self.username}"
