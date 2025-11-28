from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    contact = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"


class StudentProfile(models.Model):
    GRADE_CHOICES = (
        ('premiere', 'Première'),
        ('terminale', 'Terminale'),
        ('licence1', 'Licence 1'),
        ('licence2', 'Licence 2'),
        ('licence3', 'Licence 3'),
    )
    
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=20, unique=True, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Student: {self.user_profile.user.get_full_name()}"


class TeacherProfile(models.Model):
    SUBJECT_CHOICES = (
        ('mathematics', 'Mathematics'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('computer_science', 'Computer Science'),
        ('biology', 'Biology'),
    )
    
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id = models.CharField(max_length=20, unique=True, blank=True)
    subjects = models.CharField(max_length=100)  # Can store multiple subjects
    qualifications = models.TextField(blank=True)
    experience_years = models.IntegerField(default=0)
    bio = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Teacher: {self.user_profile.user.get_full_name()}"