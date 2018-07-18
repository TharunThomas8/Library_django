from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^enter_details/$', views.add_book, name="add-book"),
    url(r'^list_books/$', views.list_book, name="list_books"),
]