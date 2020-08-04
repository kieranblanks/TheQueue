from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    BLACK_AFRICANAMERICAN = 'Black or African American'
    WHITE_CAUCASIAN = 'White or Caucasian'
    AMERICAN_INDIAN_ALASKAN_NATIVE = 'American Indian or Alaskan Native'
    HISPANIC = 'Hispanic or Latino'
    MULTIRACIAL = 'Multiracial' 
    OTHER = 'Other'
    ETHNICITY_CHOICES = [
        (BLACK_AFRICANAMERICAN, 'Black'),
        (WHITE_CAUCASIAN, 'White or Caucasian'),
        (AMERICAN_INDIAN_ALASKAN_NATIVE, 'American Indian or Alaskan Native'),
        (HISPANIC, 'Hispanic or Latino'),
        (MULTIRACIAL, 'Multiracial'),
        (OTHER, 'Other')
    ]

    YES = 'Yes, I have a disability '
    NO = 'No, I do not have a disability'
    DISABILITY = [
        (YES, 'Yes, I have a disability'),
        (NO , 'No,t have a disability'),
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
        (LESBIAN, 'Lesbian')
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
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    username = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=15, blank=False)
    ethnicity = models.ChoiceField(max_length=40, blank=False, choices=ETHNICITY_CHOICES)
    gender = models.CharField(max_length=11, blank=False, choices=GENDER_IDENTITY)
    sexual_preference = models.CharField(max_length=50, blank=False, choices= SEXUAL_PREFERENCES)
    age = models.PositiveIntegerField(blank=False)
    email = models.CharField(max_length=125, blank=False)
    education = models.CharField(max_length=45, blank=True, choices=EDUCATION_ACHIEVED)
    disability = models.BooleanField(blank=True)

    def __str__(self):
        return self.username

