from django.contrib import admin

# Register your models here.
from . import models
 
# admin.site.register(models.booklist)
admin.site.register(models.massfile)

class booklist_admin(admin.ModelAdmin):
	list_display = ('title','available','status')

admin.site.register(models.booklist, booklist_admin)