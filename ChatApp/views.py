from django.shortcuts import render,redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('chatRoom:home')
    else:
        return redirect('users:login')    
