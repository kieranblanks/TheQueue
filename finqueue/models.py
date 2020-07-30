from django.db import models
from django import forms

# Create your models here.



# blank = false

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    username = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=15, blank=False)
    ethnicity = models.CharField(max_length= 40, blank=False)
    gender = models.CharField(max_length=11, blank=False)
    age = forms.IntegerField(blank=False)
    email = models.CharField(max_length=125, blank=False)
    education = models.CharField(max_length=45, blank=True)
    disability = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username

# class AgeRange(models.Model):
# 18-24
# 25-34
# 35-44
# 45-54
# 55-64
# 65+
def clean_age(self):
    age = self.cleaned_data.get("age")  
    if age < 18:
        raise forms.ValidationError("You must be at least 18 years old to register for The Queue")

class Ethnicity(models.Model):
    Black_AfricanAmerican = 'Black or African American'
    White_Caucasian = 'White or Caucasian'
    American_Indian_Alaskan_Native = 'American Indian or Alaskan Native'
    Hispanic = 'Hispanic or Latino'
    Multiracial = 'Multiracial' 
    Other = 'Other'
    Ethnicity_Choices = [
        (Black_AfricanAmerican, 'Black'),
        (White_Caucasian, 'White or Caucasian'),
        (American_Indian_Alaskan_Native, 'American Indian or Alaskan Native'),
        (Hispanic, 'Hispanic or Latino'),
        (Multiracial, 'Multiracial'),
        (Other, 'Other'),
    ]
ethnicity_choice = models.CharField(max_length=40, choices=Ethnicity_Choices)

class GenderIdentity(models.Model):
    Male = 'Male'
    Female = 'Female'
    Non_Binary = 'Non-Binary'
    Transgender = 'Transgender'
    Other = 'Other'
    Gender_Identity = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Non_Binary, 'Non-Binary'),
        (Other, 'Other'),
    ]
    gender_identity_options = models.CharField(max_length= 11 , choices = Gender_Identity, default=Other)


class Sexual_Preference(models.Model):
    Heterosexual = 'Heterosexual/Straight'
    Bisexual = 'Bisexual'
    Gay = 'Gay'
    Lesbian = 'Lesbian'
    Pansexual = 'Pansexual'
    Asexual =  'Asexual'
    Prefer = 'Prefer Not to Disclose'
    sexual_preferences = [
        (Heterosexual, 'Heterosexual or Straight'),
        (Bisexual, 'Bisexual'),
        (Gay, 'Gay'),
        (Lesbian, 'Lesbian')
        (Pansexual, 'Pansexual'),
        (Asexual, 'Asexual'),
        (Prefer, 'Prefer Not to Disclose'),
    ]
    sexual_preference_options = models.CharField(max_length=100, choices=sexual_preferences)

class Education(models.Model):
    Less_than_high_school_degree = 'Less than high school degree'
    High_school_degree_equivalent = 'High school degree or equivalent (e.g. GED)'
    No_degree = 'Some college but no degree'
    Associate ='Associate degree'
    Bachelor ='Bachelor degree'
    Graduate = 'Graduate degree'
    education_achieved = [
        (Less_than_high_school_degree, 'Less than high school degree'),
        (High_school_degree_equivalent, 'High school degree or equivalent (e.g. GED)'),
        (No_degree, 'Some college but no degree'),
        (Associate,'Associate degree'),
        (Bachelor, 'Bachelor degree'),
        (Graduate,'Graduate degree'),
    ]
    education_options = models.CharField(max_length=45, choices=education_achieved)

class Disability(models.Model):
    Yes = 'Yes, I have a disability'
    No = 'No, I do not have a disability'
    disability_options = models.CharField(max_length=50, blank=False)


# TRUE_FALSE_CHOICES = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ('attending',)
#         widgets = {
#             'attending': forms.Select(choices=TRUE_FALSE_CHOICES)
#         }

