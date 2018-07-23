from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^enter_many/$', views.enter_many, name="enter_many"),
    url(r'^enter_details/$', views.add_book, name="add-book"),
    url(r'^list_books/$', views.list_book, name="list_books"),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)