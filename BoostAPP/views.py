from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import UserProfile, StudentProfile, TeacherProfile
import uuid

def index(request):
   
    return render(request, 'index.html', {})



def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            # Get user type and redirect accordingly
            try:
                profile = user.profile
                if profile.user_type == 'teacher':
                    messages.success(request, f"Welcome back, Teacher {user.first_name}!")
                else:
                    messages.success(request, f"Welcome back, {user.first_name}!")
            except:
                messages.success(request, f"Welcome back!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, 'login.html')
    else:        
        return render(request, 'login.html')
 

def registration(request):
    if request.method == 'POST':
        # Common fields
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        contact = request.POST.get('contact', '')
        address = request.POST.get('address', '')
        email = request.POST['email']
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user_type = request.POST.get('user_type')  # 'student' or 'teacher'
        
        # Validate passwords match
        if password != password1:
            messages.error(request, 'Passwords do not match')
            return redirect('registration')
        
        # Check if user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already used')
            return redirect('registration')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
            return redirect('registration')
        
        try:
            # Create user
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname
            )
            user.save()
            
            # Create UserProfile
            user_profile = UserProfile.objects.create(
                user=user,
                user_type=user_type,
                contact=contact,
                address=address
            )
            
            # Create specific profile based on user type
            if user_type == 'student':
                
                student_id = f"STU{str(uuid.uuid4().int)[:8]}"
                
                StudentProfile.objects.create(
                    user_profile=user_profile,
                    student_id=student_id,

                )
                messages.success(request, f"Student registration successful! Your ID is {student_id}. Please login.")
                
            elif user_type == 'teacher':
                subjects = request.POST.get('subjects', '')
                qualifications = request.POST.get('qualifications', '')
                experience_years = request.POST.get('experience_years', 0)
                bio = request.POST.get('bio', '')
                
                teacher_id = f"TCH{str(uuid.uuid4().int)[:8]}"
                
                TeacherProfile.objects.create(
                    user_profile=user_profile,
                    teacher_id=teacher_id,
                    subjects=subjects,
                    qualifications=qualifications,
                    experience_years=experience_years,
                    bio=bio
                )
                messages.success(request, f"Teacher registration successful! Your ID is {teacher_id}. Please login.")
            
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('registration')
    else:
        return render(request, 'registration.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('index')


@login_required(login_url='login')
def profile(request):
    """View user profile"""
    user_profile = request.user.profile
    context = {
        'user_profile': user_profile
    }
    
    if user_profile.user_type == 'student':
        context['student_profile'] = user_profile.student_profile
    elif user_profile.user_type == 'teacher':
        context['teacher_profile'] = user_profile.teacher_profile
    
    return render(request, 'profile.html', context)


def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def instructors(request):
    teachers = UserProfile.objects.filter(user_type='teacher').select_related('user', 'teacher_profile')
    return render(request, 'instructors.html', {'teachers': teachers})
    

def pricing(request):
    return render(request, 'pricing.html')  

def contact(request):
    return render(request, 'contact.html')  
