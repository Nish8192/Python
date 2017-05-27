from django.conf.urls import url, include
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_email$', views.checkEmail),
    url(r'^remove/(?P<id>\d+)$', views.removeEmail)
]
