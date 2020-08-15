from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Userdetailform, Userrankform
from .models import User_rank

# Create your views here.

# Add user data from to the database 
def user_detail(request):
    user = request.user
    if request.method == 'GET':
        form = Userdetailform()
    else:
        form = Userdetailform(data=request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect(to='Rank')
    return render(request, 'user_detail.html', {"form":form})


#save ranking info to database
def user_rank(request):
    user = request.user
    if request.method == 'GET':
        form = Userrankform()
    else:
        form = Userrankform(data=request.POST)
        if form.is_valid():
            ranking = form.save(commit=False)
            ranking.user = user
            ranking.save()
            return redirect(to='Home')
    return render(request, 'user_rank.html', {"form": form})
    
#Edit User ranking data

def rank_edit(request, pk):
    ranking = User_rank.objects.get(pk=pk)
    if request.method == 'POST':
        form = Userrankform(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect(to='Home')
    else:
        form = Userrankform(instance=ranking)
        context = {'form': form}
        return render(request, 'user_rank.html', context=context)