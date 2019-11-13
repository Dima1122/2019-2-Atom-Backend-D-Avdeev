from chats.views import list_chats, create_chat
from django.urls import path

urlpatterns = [
        path('', list_chats, name='list_chats'),
        path('<str:pk>', list_chats, name='list_chats'),
        path('new/', create_chat, name='create_chat'),
]
