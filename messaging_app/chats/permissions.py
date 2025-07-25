from rest_framework import permissions

class IsOwnerOfConversation(permissions.BasePermission):
    """
    Permission to ensure the user is part of the conversation.
    """
    def has_object_permission(self, request, view, obj):
        # Assumes the Conversation model has a participants ManyToMany field
        return request.user in obj.participants.all()

class IsOwnerOfMessage(permissions.BasePermission):
    """
    Permission to ensure the user owns the message (either as sender or recipient).
    """
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.recipient == request.user
