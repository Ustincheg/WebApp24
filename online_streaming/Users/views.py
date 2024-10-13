from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .forms import LoginUser, RegisterUser
from .models import Users
def user_login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = LoginUser()
    return render(request, 'sigin.html', context={'form':form})


def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = models.User.objects.create_user(username=cd['username'], email= cd['email'], password= cd['password1'])
            user.is_active = True
            user.save()
            Users.objects.create(user = user)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUser()
    return render(request, 'register.html', context={"form":form})