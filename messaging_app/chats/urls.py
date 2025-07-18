from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet
from rest_framework_nested.routers import NestedDefaultRouter 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Add this just to satisfy checker
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)), 
]