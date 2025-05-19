from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('users:register')
    else:
        form = AuthenticationForm()    
    return render(request,"login.html",{"form":form})

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('users:login')
    else:
        form=UserCreationForm()    
    return render(request,"register.html",{"form":form})

