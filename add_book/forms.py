from django import forms
from django.contrib.auth.models import User
from . import models

class BookForm(forms.ModelForm):

    class Meta:
        model = models.booklist
        fields = ('title', 'author', 'category', 'section','file')


