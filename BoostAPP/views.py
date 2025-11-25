from django.shortcuts import render


def index(request):
    # This renders the file located at templates/home.html
    return render(request, 'index.html', {})
