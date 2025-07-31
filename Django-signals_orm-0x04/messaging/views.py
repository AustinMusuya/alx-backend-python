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


class ThreadedMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(
            parent_message__isnull=True
        ).filter(
            models.Q(sender=user) | models.Q(recipient=user)
        ).select_related(
            'sender', 'recipient'
        ).prefetch_related(
            'replies__sender', 'replies__recipient'
        )
