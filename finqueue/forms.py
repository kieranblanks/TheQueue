from django import forms
from .models import Review
from .models import Business
from users.models import User


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

class createReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'note',
        ]
        #labels = {'review':'','body':'','created':''}             

class createBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
    
        fields = [
                'name',
                'business_type',
                'location',
            ]
        
        #labels = {'name':'', 'business':'', 'location':''} 