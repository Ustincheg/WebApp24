from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from .forms import LoginUser

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