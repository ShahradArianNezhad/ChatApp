from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import JSONField 

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    joined_chatrooms = JSONField(
        default=list,
        blank=True,
        help_text="List of chat rooms with name and id"
    )

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwards):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()