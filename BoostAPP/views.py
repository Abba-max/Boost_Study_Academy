from django.shortcuts import render


def index(request):
    # This renders the file located at templates/home.html
    return render(request, 'index.html', {})

def login_view(request):
    return render(request, 'login.html', {})

def registration_view(request):
    return render(request, 'registration.html', {})