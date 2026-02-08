from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    return render(request,"registration/profile.html")

def signup(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    fm = UserCreationForm()
    return render(request,"registration/signup.html",{"form":fm})