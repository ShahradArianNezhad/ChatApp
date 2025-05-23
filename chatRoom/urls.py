from django.urls import path
from . import views

app_name='chatRoom'

urlpatterns = [
    path('',views.home,name="home"),
    path('create-room/',views.create_room,name='create_room'),
    path('join-room/',views.join_room,name="join_room"),
    path('leave-room/',views.leave_room,name='leave_room'),
    path('<str:room_name>/',views.chatroom_detail,name='chatroom_detail'),
]
