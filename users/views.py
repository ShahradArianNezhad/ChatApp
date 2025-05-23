from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import UserProfile
from django.http import JsonResponse
from django.contrib.auth.models import User

def login(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('chatRoom:home')
    else:
        form = AuthenticationForm()    
    return render(request,"login.html",{"form":form})

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('chatRoom:home')
    else:
        form=UserCreationForm()    
    return render(request,"register.html",{"form":form})

def image_upload(request):
    if request.method=="POST" and request.FILES.get('image'):
        profile=UserProfile.objects.get(user=request.user)
        profile.profile_image=request.FILES['image']
        profile.save()
        return JsonResponse({'status': 'success', 'image_url': profile.profile_image.url})
    return JsonResponse({'status': 'fail'}, status=400)

def getImageUrl(request):
    if request.method=='POST':
        profname=request.POST.get('username')
        targetUser = User.objects.get(username=profname)
        profile = UserProfile.objects.get(user=targetUser)
        return JsonResponse({'url':profile.profile_image.url})