from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('login/',views.login,name="login"),
    path('register/',views.register,name='register'),
    path('image-upload/',views.image_upload,name='image_upload'),
    path('getImageUrl/',views.getImageUrl,name='getImageUrl')
]
