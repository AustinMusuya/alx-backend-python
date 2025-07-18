from django.shortcuts import render
from .serializers import ConversationSerializer, MessageSerializer
from .models import Message, Conversation
from rest_framework import viewsets, status, filters

# authentication & Permisions api views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# viewset to perform CRUD operations

class ConversationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
    def get(self, request):
        return Response({'message': 'Hello authenticated user'}, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter]  
    ordering_fields = ['sent_at'] 

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(conversation_id=conversation_id)
        return Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
