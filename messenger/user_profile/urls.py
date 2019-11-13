from user_profile.views import user_info
from django.urls import path

urlpatterns = [
        path('', user_info, name='user_info'),
        path('<str:pk>', user_info, name='user_info')]

