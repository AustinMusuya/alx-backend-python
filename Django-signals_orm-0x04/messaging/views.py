from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse
from messaging.models import Message
from messaging.serializers import MessageSerializer
from rest_framework import generics, permissions
from django.db import models


User = get_user_model()

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return HttpResponse("Account deleted successfully.")


class ThreadedMessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(
            models.Q(sender=self.request.user) | models.Q(receiver=self.request.user)
        ).select_related('sender', 'receiver', 'parent_message').prefetch_related('replies')
