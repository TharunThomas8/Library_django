from django.db import models
from django.utils import timezone


class booklist(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    section = models.CharField(max_length=200,default="00")
    available = models.BooleanField(default='False') 
    status = models.BooleanField(default='Flase')
    file = models.FileField( default='BLANK TEXT')
    upload_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

class massfile(models.Model):
    file = models.FileField(upload_to='mass_upload/')
