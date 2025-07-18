from django.shortcuts import render
from .serializers import ConversationSerializer, MessageSerializer
from .models import Message, Conversation
from rest_framework import generics, viewsets

# authentication & Permisions api views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


# viewset to perform CRUD operations

class MessageViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def get(self, request):
        return Response({'message': 'Hello authenticated user'})


class ConversationViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
    def get(self, request):
        return Response({'message': 'Hello authenticated user'})
