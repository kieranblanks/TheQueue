from django import forms
from .models import Review
from .models import Business
from users.models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
class createuser(forms.ModelForm):
    class Meta:
        model = User 
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'ethnicity',
            'gender',
            'sexual_preference',
            'age',
            'email',
            'education',
            'disability',
        ]

def __str__(self):
    return f"{self.username}"

class createReviewForm(forms.ModelForm):
    review = models.ForeignKey()
    body = models.TextField()
    created = models.DateTimeFields(auto_now_add=True)
    class Meta:
        model = Review
        fields = [
            'review',
            'body',
            'created',
        ]
        labels = {'review':'','body':'','created':''}             

class createBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
    
    BUSINESS_TYPE = [
        (HEALTHCARE, 'Healthcare'),
        (RESTAURANTS, 'Restaurants'),
        (SHOPPING, 'Shopping'),
        (EDUCATION, 'Education'),
    ]

    fields = [
            'name',
            'business_type',
            'location',
        ]
        
    labels = {'name':'', 'business':'', 'location':''}
    def __str__(self):
        return f"{self.business_name}"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               