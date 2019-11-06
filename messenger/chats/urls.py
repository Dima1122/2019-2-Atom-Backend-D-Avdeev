from chats.views import chat_list
from django.urls import path

urlpatterns = [
        path('', chat_list, name='chat_list'),
        path('<int:pk>', chat_list, name='chat_list'),
]
