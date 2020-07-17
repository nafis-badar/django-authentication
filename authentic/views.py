from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request,'index.html')

def signup(request):
    form =CreateUserForm()
    if request.method== 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for" + user)
            return redirect('login')



    return render(request,'registration.html',{"form":form})

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or password is incorrect")

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')







