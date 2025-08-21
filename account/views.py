from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm, ResumeUploadForm
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings
import os

STATIC_BUILD = getattr(settings, "STATIC_BUILD", False)
def navbar(request):
    return render(request,'navbar.html')
def home(request):
    return render(request, "home.html")

def register(request):
    if not STATIC_BUILD and request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
             # Send welcome email to the user
            user_subject = "Welcome to our SustainCred Job Portal platform!"
            user_message = f"Hi {user.username},\n\nThank you for registering!\n\nBest Regards,\nTeam"
            send_mail(user_subject, user_message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

            # Send notification email to admin
            admin_subject = "New Registration"
            admin_message = f"New user registered:\n\nUsername: {user.username}\nEmail: {user.email}"
            send_mail(admin_subject, admin_message, settings.EMAIL_HOST_USER, ['nnavaneetha557@gmail.com'], fail_silently=False)

            # Redirect to home page
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if not STATIC_BUILD and request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def upload_resume(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, 'upload_resume.html', {'form': form, 'success': True, 'profile': profile})
    else:
        form = ResumeUploadForm(instance=profile)
    return render(request, 'upload_resume.html', {'form': form, 'profile': profile})

@login_required
def delete_resume(request):
    profile = request.user.profile  
    if profile.resume:
        profile.resume.delete(save=False) 
        profile.resume = None
        profile.save()
    return redirect('upload_resume')

def user_logout(request):
    logout(request) 
    return redirect('home')  