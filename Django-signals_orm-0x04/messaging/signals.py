from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance, user=instance.receiver)



@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if not instance._state.adding:  # This means it's being updated, not created
        try:
            old_instance = Message.objects.get(pk=instance.pk)
            if old_instance.content != instance.content:
                MessageHistory.objects.create(
                    message=old_instance,
                    old_content=old_instance.content
                )
                instance.edited = True  # Mark message as edited
        except Message.DoesNotExist:
            pass  # This might occur rarely in race conditions

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete messages where user was sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete notifications
    Notification.objects.filter(user=instance).delete()

    # Delete message history edits made by this user
    MessageHistory.objects.filter(edited_by=instance).delete()