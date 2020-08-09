from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import createBusinessForm, createReviewForm
from django.shortcuts import get_object_or_404
from .models import Business
# Create your views here.

def home(request):
    return render(request, 'home.html')

def single_business(request,pk):
    business = get_object_or_404(Business, pk=pk)
    return render(request, 'business_detail.html',{'business': business})
    

def list_businesses(request):
    businesses = Business.objects.all()
   # recommendation = businesses.user
    #this is where calculation and matching will happen 
    return render(request, "list_businesses.html",{'reviews':reviews})

def add_business(request):
     if request.method == 'GET':
       form = createBusinessForm()
     else:
        form = createBusinessForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_businesses')
     return render(request, 'add_business.html', {"form":form})

def new_review(request):
    #create new review
    if request.model != 'POST':
        #No data submitted, create a blank form.
        form = ReviewForm()
    else:
        #Post data submitted; process data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_businesses')
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'new_review.html', context)
    
#Computations goes here
#create a loop multiply
#create loop to  add
#see album examples 