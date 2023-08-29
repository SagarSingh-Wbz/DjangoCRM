from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    #Check if user is logged in
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate User
        userAuth=authenticate(request,username=username, password=password)
        if userAuth is not None:
            login(request, userAuth)
            messages.success(request,"You have been logged in!")
            return redirect("home")
        else:
            messages.error(request,"Your credentials are invalid. Please try again...")
            return redirect("home")
    else:
        return render(request,'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request,"register.html",{})