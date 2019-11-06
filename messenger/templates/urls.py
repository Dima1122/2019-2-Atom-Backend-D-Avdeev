from templates.views import main_page
from django.urls import path

urlpatterns = [
        path('', main_page, name='main_page'),
]
