# from .models import Race
from django import forms
from django.contrib.auth.models import UserRegistration
from django.contrib.auth.forms import 
from .models import UserRegistration


class createuserForm(forms.ModelForm):
    class Meta:
        model = _ 
        fields = [
            'first_name',
            'last_name'
            'username',
            'password',
            'ethnicity',
            'gender',
            'age',
            'email',
            'education',
            'disability',
        ]



def __str__(self):
    return f"{self.username}"
