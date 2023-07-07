from django.shortcuts import render
from .models import User


# Create your views here.
def login(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')
