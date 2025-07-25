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


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of the conversation.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Called when checking access to a specific object.
        Works for both Conversation and Message instances.
        """
        if hasattr(obj, 'participants'):
            # Conversation instance
            return request.user in obj.participants.all()
        elif hasattr(obj, 'conversation'):
            # Message instance
            return request.user in obj.conversation.participants.all()
        return False
