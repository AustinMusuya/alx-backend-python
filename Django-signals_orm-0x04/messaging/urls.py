from .views import delete_user,  ThreadedMessagesView
from django.urls import path

urlpatterns = [
    path('delete-account/', delete_user, name='delete_user'),
    path('messages/threaded/', ThreadedMessagesView.as_view(), name='threaded-messages'),
]
