from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def index(request):
    # This renders the file located at templates/home.html
    return render(request, 'index.html', {})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome back, {user.firstname}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, 'login.html')
    else:        
        return render(request, 'login.html')
 

def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        contact = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('registration')
            elif User.objects.filter(firstname=firstname).exists():
                messages.info(request, 'Username Already Used')
                return redirect('registration')
            else:
                user = User.objects.create_user(firstname=firstname, lastname=lastname,contact=contact,address=address, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Welcome to Eyang Estate.")
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
