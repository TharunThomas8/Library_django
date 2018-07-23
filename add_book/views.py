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
				# formed = {
				# "title" : "zzz",
				# "author" : "zzz",
				# "category" : "zzz",
				# "section" : "zzz",
				# "available" : True,
				# "status" : True,
				# "file" : "BLANK TEXT"
				# }
				# print (formed)
				# m = models.booklist(**formed)
				forms.save()
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

def enter_many(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
			return HttpResponse("Successful")

		else:
			form = ExampleForm()
			return render(request, 'library/file.html', {'form': form})
	else:
		return HttpResponse("you need to be an admin to view this")

def handle_uploaded_file(file, filename):
	form = {
				"title" : "",
				"author" : "",
				"category" : "",
				"section" : "",
				"available" : True,
				"status" : True,
				"file" : "BLANK TEXT"
				}
	for s in file.read().split(','):
		for i in range(1,7):
			if(i==1):
				form["title"] = s
			if(i==2):
				form["author"] = s
			if(i==3):
				form["category"] = s
			if(i==4):
				form["section"] = s
			if(i==5):
				form["available"] = s
			if(i==6):
				form["status"] = s
			if(i==7):
				form["file"] = s
				m = models.booklist(**form)
				m.save()
