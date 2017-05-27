from django.conf.urls import url
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_product$', views.addProduct),
    url(r'edit/(?P<id>\d+)$', views.editProduct),
    url(r'view/(?P<id>\d+)$', views.showProduct),
    url(r'remove/(?P<id>\d+)$', views.removeProduct),

    url(r'edit/(?P<id>\d+)/update$', views.updateProduct),
    url(r'^add_product/add$', views.createProduct)
]
