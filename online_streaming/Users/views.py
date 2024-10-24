from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, models
from django.urls import reverse
from .forms import LoginUser, RegisterUser
from .models import Users, EmailToken
from .tasks_celery import sending_email
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password') 
    else:
        form = LoginUser()
    
    return render(request, 'sigin.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def user_register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = models.User.objects.create_user(
                    username=cd['username'],
                    email=cd['email'],
                    password=cd['password1']
                )
                user.is_active = False
                user.save()
                
                token = EmailToken.objects.create(user=user)
                link_activate = request.build_absolute_uri(reverse('confirm-email', args=[str(token.token)]))
                sending_email(link=link_activate, email_user=user.email)
                messages.success(request, f"Письмо успешно отправлено на почту {user.email}!")
                return redirect('register')
            except Exception as e:
                form.add_error(None, f'Error during registration: {str(e)}') 
    else:
        form = RegisterUser()
    
    return render(request, 'register.html', {'form': form})


def confirm_email(request, token):
    confirm_token = get_object_or_404(EmailToken, token=token)
    user = confirm_token.user
    user.is_active = True
    user.save()

    Users.objects.create(user=user)  

    confirm_token.delete()
    login(request, user)
    
    return redirect('home')
