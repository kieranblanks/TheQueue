from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Business(models.Model):
#Establishment categories 
    HEALTHCARE = 'Healthcare'
    RESTAURANTS = 'Restaurants'
    SHOPPING = 'Shopping'
    EDUCATION = 'Education'
    BUSINESS_TYPE = [
        (HEALTHCARE, 'Healthcare'),
        (RESTAURANTS, 'Restaurants'),
        (SHOPPING, 'Shopping'),
        (EDUCATION, 'Education'),
    ]

    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=40, choices=BUSINESS_TYPE)
    Location = models.CharField(max_length=64)
    
    def __str__(self):
        return str(self.Name)

class Review(models.Model):
    ethnicity = models.IntegerField()
    age = models.IntegerField()
    orientation = models.IntegerField()
    gender = models.IntegerField()
    disability = models.IntegerField()
    education = models.IntegerField()
    business = models.ForeignKey(to='Business',on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(to='User',on_delete=models.CASCADE, related_name='reviews')
    timestamp = models.DateTimeField(auto_now_add=False)
    note = models.TextField()



