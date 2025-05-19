from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import JSONField 

User = get_user_model()

class ChatRoom(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="The name of the chat room"
    )
    
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        help_text="When the room was created"
    )
    
    members = JSONField(
        default=list,
        blank=True,
        help_text="List of chat rooms with name and id"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Chat Room"
        verbose_name_plural = "Chat Rooms"
    
    def __str__(self):
        return f"{self.members}"