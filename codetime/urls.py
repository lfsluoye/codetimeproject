from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.loginForm, name='loginForm'),
    url(r'^product/$', views.productForm, name='productForm'),
]