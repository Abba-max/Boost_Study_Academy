from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def index(request):
   
    return render(request, 'index.html', {})



def login(request):
    if request.method == 'POST':
        username = request.POST['email']  # Using email as username
        password = request.POST['password']
        
      
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome back, {user.first_name if user.first_name else user.username}!")
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
        contact = request.POST.get('contact', '')
        address = request.POST.get('address', '')
        email = request.POST['email']
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        

        if password == password1:
        
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Username(Email) Already Used')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('registration')
            else:
                
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=firstname,
                    last_name=lastname
                )
                user.save()
                messages.success(request, "Registration successful! Please login.")
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('index')


def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def instructors(request):
    return render(request, 'instructors.html')  

def pricing(request):
    return render(request, 'pricing.html')  

def contact(request):
    return render(request, 'contact.html')  
