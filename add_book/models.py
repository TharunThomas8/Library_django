from django.db import models
from django.utils import timezone


# Create your models here.

class booklist(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    upload_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title