from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.

def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in")
    else:
        if request.method == 'POST':
            form = forms.Register(request.POST)
            if form.is_valid():
                form.save()
                models.Otherdetail(
                user=User.objects.get(username=form.cleaned_data.get('username')),
                bio=form.cleaned_data.get('bio'),
                dob=form.cleaned_data.get('date_of_birth')
                ).save()
                return HttpResponse("user saved")
            else:
                return render(request, 'user_app/signup.html', {'form': form})
        else:
            form = forms.Register()
        return render(request, 'user_app/signup.html', {'form': form})

def sign_in(request):
    if request.user.is_authenticated:
        print ("here")
        return render(request, 'user_app/home.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,
             password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to music list page.
                    return render(request, 'user_app/home.html')
                else:
                    return render(request, 'user_app/login.html', {'err': 'Your account is banned'})
            else:
                return render(request, 'user_app/login.html', {'err': 'Wrong credentials provided'})
        else:
            return render(request, 'user_app/login.html', {'err': ''})
