from chat_page.views import chat, send_message, get_message, read_chat
from django.urls import path

urlpatterns = [
        path('', chat, name='chat'),
        path('<int:pk>', chat, name='chat'),
        path('new_message/', send_message, name='send_message' ),
        path('get_messages/', get_message, name='get_message'),
        path('read_chat/', read_chat, name='read_chat')]

