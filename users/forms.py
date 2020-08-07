from django import forms
from django.contrib.auth.models import UserRegistration
# from django.contrib.auth.forms import  (which forms are we supposed to be pulling from)
from user.models import UserReg

class createuserForm(forms.ModelForm):
    ETHNICITY_CHOICES = (
        (BLACK_AFRICANAMERICAN, 'Black'),
        (WHITE_CAUCASIAN, 'White or Caucasian'),
        (AMERICAN_INDIAN_ALASKAN_NATIVE, 'A1merican Indian or Alaskan Native'),
        (HISPANIC, 'Hispanic or Latino'),
        (MULTIRACIAL, 'Multiracial'),
        (OTHER, 'Other')
    )
    GENDER_IDENTITY = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
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
        model = UserReg
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
