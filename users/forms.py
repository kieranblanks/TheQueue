from django import forms
from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class createUserForm(forms.ModelForm):
    ETHNICITY_CHOICES = (
        (BLACK_AFRICANAMERICAN, 'Black or African American'),
        (WHITE_CAUCASIAN, 'White or Caucasian'),
        (AMERICAN_INDIAN_ALASKAN_NATIVE, 'American Indian or Alaskan Native'),
        (ASIAN, 'Asian or Asian American'),
        (HISPANIC, 'Hispanic or Latino'),
        (MULTIRACIAL, 'Multiracial'),
        (OTHER, 'Other')
    )
    GENDER_IDENTITY = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANSGENDER, 'Transgender'),
        (NON_BINARY, 'Non-Binary'),
        (OTHER, 'Other'),
    ]
    EDUCATION_ACHIEVED = [
        (LESS_THAN_HIGH_SCHOOL_DEGREE, 'Less than high school degree'),
        (HIGH_SCHOOL_DEGREE_EQUIVALENT, 'High school degree or equivalent (e.g. GED)'),
        (NO_DEGREE, 'Some college but no degree'),
        (ASSOCIATE,'Associate degree'),
        (BACHELOR, 'Bachelor degree'),
        (GRADUATE,'Graduate degree'),
    ]
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)
    ethnicity = forms.ChoiceField(choices=ETHNICITY_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_IDENTITY)
    age = forms.PositiveIntegerField()
    email = forms.EmailField()
    education = forms.ChoiceField(choices=EDUCATION_ACHIEVED)
    disability = forms.BooleanField()

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
