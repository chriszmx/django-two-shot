from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth.models import User


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid login credentials.')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


# TypeError: 'builtin_function_or_method' object is not subscriptable
# check this folder... had .get which i didnt nead


def logout_view(request):
    logout(request)
    return redirect('login')


# feature 10 signup


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            if password == password_confirmation:
                user = User.objects.create_user(username=username,
                                                password=password)
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'the passwords do not match')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
