from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^gen_rand_word$', views.generateRandWord),
    url(r'^reset$', views.reset)
]
