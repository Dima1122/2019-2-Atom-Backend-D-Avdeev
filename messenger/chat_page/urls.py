from chat_page.views import chat
from django.urls import path

urlpatterns = [
        path('', chat, name='chat'),
        path('<int:pk>', chat, name='chat')]

