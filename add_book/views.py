from django.shortcuts import render
from . import models
from . import forms
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def add_book(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			form = forms.BookForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse("book saved")
		else:
			form = forms.BookForm()
		return render(request, 'library/input.html', {'form': form})
	else:
		return HttpResponse("you need to be an admin to view this")

def list_book(request):
    if request.user.is_superuser:
        book = models.booklist.objects.all()
        return render(request, 'library/list.html',{'entry':book})
    else:
        return HttpResponse("you need to be an admin to view this")