from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import createBusinessForm, createReviewForm
from django.shortcuts import get_object_or_404
from .models import Business
from django.db.models import Avg
# Create your views here.

def home(request):
    return render(request, 'home.html')

def single_business(request,pk):
    business = get_object_or_404(Business, pk=pk)  #finds a business based on pk
    reviews = business.reviews.all()  #list of reviews for all business
    review_notes= [ review.note for review in reviews  ] #python list comprehension 
    return render(request, 'business_detail.html',
    {'business': business, 'reviews': reviews, 'averages': average_review(business)})

#Aggregate average relative perception
def average_review(business): #reusable average code..for other purposes
    reviews = business.reviews.all()
    averages = {
        'Ethnicity' : reviews.aggregate(Avg('ethnicity'))['ethnicity__avg'],
        'Gender' : reviews.aggregate(Avg('gender'))['gender__avg'],
        'Disability' : reviews.aggregate(Avg('disability'))['disability__avg'],
        'Orientation' : reviews.aggregate(Avg('orientation'))['orientation__avg'],
        'Age' : reviews.aggregate(Avg('age'))['age__avg'],
        'Education': reviews.aggregate(Avg('education'))['education__avg'],
        }
    return averages


def list_businesses(request,pk):
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

#Step 1 of dot product-finding product of user relative importance and business average
# def dot_prod(user_rank, average):
#     combined_lists = zip(user_rank, average)
#     products = [ pair[0]*pair[1] for pair in combined_lists]
# return sum(products)


#First, create dictionary for user ranking see averages
#Create a form on recommendations page to let users select business type
#django filters 
#run django query to find all restaurants-->Business.objects.filter(e.g. restaurant)
#return a list restaurants from the business.objects....
#loop through query set using previously defined avg. function
#return averages ratings for each
#as a part of the for loop do the dot product to align with user rankings

#Primary goal: enter a biz type and render the results
#ask about using dictionaries for dot product 
#how will i keep track of the recommendations?
#think about how the dot product will be sorted

#write a loop to run dot products per biz type








