from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserForm
# from users import views
# from django.contrib.auth forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(response):
    if response.method == "GET":
        form = createUserForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = createUserForm

    return render(response, "users/userreg/signup.html", {"form":form})        


def signup_view(request):
    form = createUserForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})

def clean_age(self):
    age = self.cleaned_data.get("age")  
    if age < 18:
        raise forms.ValidationError("You must be at least 18 years old to register for The Queue.")

#parking validation for reference. do without validation and then add that in later

