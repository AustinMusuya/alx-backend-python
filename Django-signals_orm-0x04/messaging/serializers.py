from rest_framework import serializers
from .models import Message

class RecursiveMessageSerializer(serializers.Serializer):
    def to_representation(self, value):
        return MessageSerializer(value, context=self.context).data

class MessageSerializer(serializers.ModelSerializer):
    replies = RecursiveMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp', 'parent_message', 'replies']
