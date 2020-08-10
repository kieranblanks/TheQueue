from django import forms
from users.models import User, User_rank
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate


class Userdetailform(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                'ethnicity',
                'gender',
                'age',
                'education',
                'disability',
                ]

class Userrankform(forms.ModelForm):
    class Meta:
        model = User_rank
        fields = [
                'ethnicity',
                'gender',
                'orientation',
                'age',
                'education',
                'disability',
                ]

