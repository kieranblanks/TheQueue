from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    BLACK_AFRICANAMERICAN = 'Black or African American'
    WHITE_CAUCASIAN = 'White or Caucasian'
    AMERICAN_INDIAN_ALASKAN_NATIVE = 'American Indian or Alaskan Native'
    HISPANIC = 'Hispanic or Latino'
    ASIAN = 'Asian or Asian American'
    MULTIRACIAL = 'Multiracial' 
    OTHER = 'Other'
    ETHNICITY_CHOICES = [
        (BLACK_AFRICANAMERICAN,'Black or African American'),
        (WHITE_CAUCASIAN, 'White or Caucasian'),
        (AMERICAN_INDIAN_ALASKAN_NATIVE, 'American Indian or Alaskan Native'),
        (HISPANIC, 'Hispanic or Latino'),
        (ASIAN, 'Asian or Asian American'),
        (MULTIRACIAL, 'Multiracial'),
        (OTHER, 'Other'),
    ]

    MALE = 'Male'
    FEMALE= 'Female'
    NON_BINARY = 'Non-Binary'
    TRANSGENDER = 'Transgender'
    OTHER = 'Other'
    GENDER_IDENTITY = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Non-Binary'),
        (TRANSGENDER, 'Transgender'),
        (OTHER, 'Other'),
    ]

    HETEROSEXUAL = 'Heterosexual or Straight'
    BISEXUAL = 'Bisexual'
    GAY = 'Gay'
    LESBIAN = 'Lesbian'
    PANSEXUAL = 'Pansexual'
    ASEXUAL =  'Asexual'
    PREFER = 'Prefer Not to Disclose'
    SEXUAL_PREFERENCES = [
        (HETEROSEXUAL, 'Heterosexual or Straight'),
        (BISEXUAL, 'Bisexual'),
        (GAY, 'Gay'),
        (LESBIAN, 'Lesbian'),
        (PANSEXUAL, 'Pansexual'),
        (ASEXUAL, 'Asexual'),
        (PREFER, 'Prefer Not to Disclose'),
    ]
    LESS_THAN_HIGH_SCHOOL_DEGREE = 'Less than high school degree'
    HIGH_SCHOOL_DEGREE_EQUIVALENT = 'High school degree or equivalent (e.g. GED)'
    NO_DEGREE = 'Some college but no degree'
    ASSOCIATE ='Associate degree'
    BACHELOR ='Bachelor degree'
    GRADUATE = 'Graduate degree'
    EDUCATION_ACHIEVED = [
        (LESS_THAN_HIGH_SCHOOL_DEGREE, 'Less than high school degree'),
        (HIGH_SCHOOL_DEGREE_EQUIVALENT, 'High school degree or equivalent (e.g. GED)'),
        (NO_DEGREE, 'Some college but no degree'),
        (ASSOCIATE,'Associate degree'),
        (BACHELOR, 'Bachelor degree'),
        (GRADUATE,'Graduate degree'),
    ]
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=15)
    ethnicity = models.CharField(max_length=40, choices=ETHNICITY_CHOICES)
    gender = models.CharField(max_length=11, blank=False, choices=GENDER_IDENTITY)
    sexual_preference = models.CharField(max_length=50, choices= SEXUAL_PREFERENCES)
    age = models.PositiveIntegerField(blank=False, default=0)
    email = models.CharField(max_length=125)
    education = models.CharField(max_length=45, blank=True, choices=EDUCATION_ACHIEVED)
    disability = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.username

