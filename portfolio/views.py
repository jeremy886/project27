from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'portfolio/register.html', {'form': form})


# Login view
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a successful login page
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})
