from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from models import Conversation, Message

User = get_user_model()

# Create User serializer class


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}}


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender','conversation', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages','created_at']
