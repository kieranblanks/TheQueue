from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .forms import createBusinessForm, createReviewForm
from django.shortcuts import get_object_or_404
from .models import Business
from users.models import User_rank
from django.db.models import Avg
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, 'home.html')

def single_business(request,pk):
    business = get_object_or_404(Business, pk=pk)  #finds a business based on pk
    reviews = business.reviews.all()  #list of reviews for all business
    review_notes= [ review.note for review in reviews  ] #python list comprehension 
    return render(request, 'business_detail.html',
    {'business': business, 'reviews': reviews, 'averages': average_review(business)})

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

# Dictionary for user ranking see averages 
def user_ranking(request, user):
    businesses = Business.objects.all()
    user_rank = User_rank.objects.get(user=request.user)
    user_recom = []
    for business in businesses:
        averages = business.average_review
        dot_product = {
            'Ethnicity' : averages['Ethnicity'] * user_rank.ethnicity,
            'Gender' : averages['Gender'] * user_rank.gender,
            'Disability' : averages['Disability'] * user_rank.disability,
            'Orientation' : averages['Orientation'] * user_rank.orientation,
            'Age' : averages['Age'] * user_rank.age,
            'Education': averages['Education'] * user_rank.education,
            }
        sum = 0
        for value in dot_product.values():
            print(value)
            sum += value

        user_recom.append((business, sum)) #appending them as tuples to the list
    return user_recom

def recommendation(request):
    current_user = request.user 
    recommendations = user_ranking(request, user=request.user)
    context = {'recommendations':recommendations}
    return render(request, 'recommendations.html', context=context)


    def search(request):
    if request.method == 'GET':
        search = request.Get.get('search')
        results = Business.objects.filter(business_name=search)
        return render(request, 'search.html', {'results':results})

class SearchResultsView(ListView):
model = Business
template_name = 'recommendations.html'

    def get_queryset(self):
        return Business.objects.filter(Q(name__icontains='Foodgenix'))



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










