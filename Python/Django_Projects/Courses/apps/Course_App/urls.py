from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.addCourse),
    url(r'^delete/(?P<id>\d+)$', views.deleteCourse)
]
