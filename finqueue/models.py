from django.db import models
from django import forms
from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth import get_user_model
from django.db.models import Avg

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

    name = models.CharField(max_length=50)
    business_type = models.CharField(max_length=40, choices=BUSINESS_TYPE)
    location = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)

    #Aggregate average relative perception
    @property
    def average_review(self): #reusable average code..for other purposes
        reviews = self.reviews.all()
        averages = {
            'Ethnicity' : reviews.aggregate(Avg('ethnicity'))['ethnicity__avg'],
            'Gender' : reviews.aggregate(Avg('gender'))['gender__avg'],
            'Disability' : reviews.aggregate(Avg('disability'))['disability__avg'],
            'Orientation' : reviews.aggregate(Avg('orientation'))['orientation__avg'],
            'Age' : reviews.aggregate(Avg('age'))['age__avg'],
            'Education': reviews.aggregate(Avg('education'))['education__avg'],
            }
        return averages

class Review(models.Model):
    ethnicity = models.IntegerField()
    age = models.IntegerField()
    orientation = models.IntegerField()
    gender = models.IntegerField()
    disability = models.IntegerField()
    education = models.IntegerField()
    business = models.ForeignKey(to='Business',on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='reviews')
    timestamp = models.DateTimeField(auto_now_add=False)
    note = models.TextField()
    
   

   




