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

def enter_many(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			form = forms.ExampleForm( request.POST,request.FILES)
			form.save()
			name = request.FILES['file'].name
			s = "/home/tta/Documents/lib_django/library/media/mass_upload/"+name
			File_object = open(s,"r")
			f = File_object.read()
			format = {
				"title" : "",
				"author" : "",
				"category" : "",
				"section" : "",
				"available" : True,
				"status" : True,
				"file" : "BLANK TEXT"
				}
			print (f)
			i=1
			print (i)
			for s in f.split(','):
				print (i)
				if(i==1):
					format["title"] = s
					i=i+1
				elif(i==2):
					format["author"] = s
					i=i+1
				elif(i==3):
					format["category"] = s
					i=i+1
				elif(i==4):
					format["section"] = s
					i=i+1
				elif(i==5):
					format["available"] = s
					i=i+1
				elif(i==6):
					format["status"] = s
					i=i+1
				else:
					format["file"] = s
					m = models.booklist(**format)
					print (i)
					m.save()
					i=1
			return HttpResponse("Success")

		else:
			form = forms.ExampleForm()
			return render(request, 'library/file.html', {'form': form})
	else:
		return HttpResponse("you need to be an admin to view this")

