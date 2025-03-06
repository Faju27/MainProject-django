from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect('/')
