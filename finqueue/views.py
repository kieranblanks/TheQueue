from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import createBusinessForm, createReviewForm
from .forms import MyCustomForm
# Create your views here.
def home(request):
    return render(request, 'home.html'),

def list_business(request):
    reviews = Business.objects.all()
    return render(request, "list_business.html",{'"reviews':reviews})

def add_business(request):
     if request.method == 'GET':
       form = createBusinessForm()
     else:
        form = createBusinessForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_business')
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
            return redirect('list_business')
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'new_review.html', context)
    
