from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 

# Create your models here.
ROLE_CHOICES = [
    ('guest', 'Guest'),
    ('host', 'Host'),
    ('admin', 'Admin'),
]

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    email = models.EmailField(unique=True, db_index=True)
    username = None # Overriding username related fields. Using email as Unique ID
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, default='guest', max_length=10)
    password_hash = models.CharField(max_length=128)
    USERNAME_FIELD = 'email' # Using email as the unique Identifier
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['sent_at']
        indexes = [
            models.Index(fields=['sender_id', 'sent_at']),
        ]
    
    def __str__(self):
        return f"Message from {self.sender} in {self.sender_id}" 

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    participants_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]
    def __str__(self):
        return f"Conversation {self.conversation_id}"
