from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models
import logging

def user(request, username):
    try:
        logger = logging.getLogger(__name__)
        user_to_use = User.objects.get(username=username)
        logger.error('USERNAME: ' + user_to_use.username)
        logger.error('ID: ' + str(user_to_use.id))

        # posts = Post.objects.filter(author=user_to_use.id).order_by('-votes_total')

        return render(request, 'accounts/user.html', {"error":"User " + username + " does not exist."})
        # return render(request, 'accounts/user.html', {'user':user_to_use,'posts':posts})
    except User.DoesNotExist:
        return render(request, 'accounts/user.html', {"error":"User " + username + " does not exist."})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {"error":"Username has already been taken."})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {"error":"Passwords didn't match."})
        
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            # Invalid
            return render(request, 'accounts/login.html', {"error":"The username and password didn't match."})
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')