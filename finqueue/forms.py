from django import forms
# from .models import Race

class createuser(forms.ModelForm):
    class Meta:
        model = _ 
        fields = [
            'username'
        ]



def __str__(self):
    return f"{self.username}"