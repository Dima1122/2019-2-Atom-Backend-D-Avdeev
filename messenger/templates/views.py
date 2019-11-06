from django.shortcuts import render
from .forms import UserForm
 
def main_page(request):
    userform = UserForm()
    return render(request, "index.html", {"form": userform})
