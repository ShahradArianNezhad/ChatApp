from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from chatRoom.models import ChatRoom
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

# Create your views here.


@login_required
def home(request):
    userProfile = UserProfile.objects.get(user=request.user)
    chats=[]
    for i in userProfile.joined_chatrooms:
        chats.append(ChatRoom.objects.get(name=i))
        
    return render(request,'home.html',{"chatrooms":chats,'userProfile':userProfile})

@csrf_exempt
def create_room(request):
    if request.method=="POST":
        room_name=request.POST.get('room_name')
        if room_name:
            userProfile = UserProfile.objects.get(user=request.user)
            newRoom=ChatRoom.objects.create(name=room_name)
            userProfile.joined_chatrooms.append(newRoom.name)
            userProfile.save()
            newRoom.members.append(request.user.username)
            newRoom.save()
            return JsonResponse({
                'status':'success',
                'room_name':newRoom.name,
            })
    return JsonResponse({'status':'error'}) 


def join_room(request):
    if request.method=='POST':
        room_name = request.POST.get('room_name')
        if room_name:
            userProfile = UserProfile.objects.get(user=request.user)
            try:
                FoundRoom=ChatRoom.objects.get(name=room_name)
            except:
                return JsonResponse({
                    'status':'not found'
                })  
            if FoundRoom:
                userProfile.joined_chatrooms.append(FoundRoom.name)
                FoundRoom.members.append(request.user.username)
                userProfile.save()
                FoundRoom.save()
                return JsonResponse({
                'status':'success'})
            else:
                return JsonResponse({
                    'status':'not found'
                })


def leave_room(request):

    if request.method=='POST':
        room_name = request.POST.get('room_name')
        if room_name:
            userProfile=UserProfile.objects.get(user=request.user)
            foundRoom=ChatRoom.objects.get(name=room_name)
            if foundRoom:
                userProfile.joined_chatrooms.remove(room_name)
                foundRoom.members.remove(request.user.username)
                userProfile.save()
                foundRoom.save()
                return JsonResponse({
                    'status':'success'
                })
    return JsonResponse({
        'status':'fail'
    })







def chatroom_detail(request,room_name):
    userProfile = UserProfile.objects.get(user=request.user)
    chats=[]
    for i in userProfile.joined_chatrooms:
        chats.append(ChatRoom.objects.get(name=i))


    chatroom = get_object_or_404(ChatRoom,name=room_name)
    messages =chatroom.messages

    enriched_messages =[]
    for msg in messages:
        try:
            messageProfile = User.objects.get(username=msg['sender'])
            messageProfile= UserProfile.objects.get(user=messageProfile)
            profile_image_url = messageProfile.profile_image.url

        except:    
            profile_image_url = '/media/profile_images/default.png'
        enriched_messages.append({
            'sender': msg['sender'],
            'message': msg['message'],
            'time_sent': msg['time_sent'],
            'image_url': profile_image_url
        })    



    if room_name in userProfile.joined_chatrooms:
        return render(request,'chatroom_detail.html',{'chatroom':chatroom,"chatrooms":chats,'messages':messages,'userProfile':userProfile,'enrichedMessages':enriched_messages})
    raise PermissionDenied