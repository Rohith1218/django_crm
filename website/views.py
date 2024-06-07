from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            messages.success(req,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(req,"There was an error logging in...")
            return redirect('home')
    else:    
        return render(req, 'home.html', {})


def logout_user(req):
    logout(req)
    messages.success(req, "Logged out...")
    return redirect('home')
