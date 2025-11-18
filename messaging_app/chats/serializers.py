# imports
from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'role']
    pass

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'sender', 'message_body']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']

