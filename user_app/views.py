from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from add_book.models import booklist
from add_book.forms import BookForm

# Create your views here.
def list_book(request):
    if request.user.is_authenticated:
        book = booklist.objects.all()
        return render(request, 'library/list.html',{'entry':book})
    else:
        return HttpResponse("you need to be an admin to view this")


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
                    return render(request, 'user_app/home.html')
                else:
                    return render(request, 'user_app/login.html', {'err': 'Your account is banned'})
            else:
                return render(request, 'user_app/login.html', {'err': 'Wrong credentials provided'})
        else:
            return render(request, 'user_app/login.html', {'err': ''})

def dnt_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("book saved")
            else:
                return HttpResponse(form.errors)
        else:
            form = BookForm()
        return render(request, 'user_app/input.html', {'form': form})
    else:
        return HttpResponse("you need to be a user ")
