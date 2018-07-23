from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^dnt_book/$', views.dnt_book, name="dnt_book"),
    url(r'^list_books/$', views.list_book, name="list_books"),
    url(r'^sign_up/$', views.sign_up, name="sign_up"),
    url(r'^sign_in/$', views.sign_in, name="sign_in"),
    url(r'^sign_out/$', auth_views.logout, {'template_name': 'user_app/logout.html'}),
    url(r'^home/$', TemplateView.as_view(template_name='user_app/home.html')),
]