from django.test import TestCase
from django.contrib.auth import get_user_model
from messaging.models import Message, Notification

User = get_user_model()

class SignalTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', email="user1@mail.com", password='pass')
        self.receiver = User.objects.create_user(username='receiver', email="user2@mail.com", password='pass')

    def test_notification_created_on_message_send(self):
        msg = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Test message"
        )
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, msg)
