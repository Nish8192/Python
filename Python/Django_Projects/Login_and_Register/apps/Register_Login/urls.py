from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user$', views.createUser),
    url(r'^login$', views.logIn),
    url(r'^home$', views.index)
]
