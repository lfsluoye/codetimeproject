from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^login/aciton$', views.login_action, name='login_action'),
    url(r'^product/$', views.product),
]