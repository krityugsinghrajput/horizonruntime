from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'debugfinder/home.html')


def server_status(request):
    return render(request, 'debugfinder/server_status.html')


def login(request):
    context = {
    'Hey there, login successful {user}'
    }
    return render('debugfinder/login.html', context)