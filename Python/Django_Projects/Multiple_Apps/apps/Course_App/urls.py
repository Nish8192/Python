from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_course$', views.addCourse, name='add_course'),
    url(r'^delete/(?P<id>\d+)$', views.deleteCourse, name='delete')
]
