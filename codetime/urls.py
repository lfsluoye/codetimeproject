from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.loginForm, name='loginForm'),
    url(r'^product/$', views.productForm, name='productForm'),
    url(r'^orderSearch/$', views.orderSearch, name='orderSearch'),
    url(r'^changeShipments/$', views.changeShipments, name='changeShipments'),
    url(r'^changeStatus/$', views.changeStatus, name='changeStatus'),
    url(r'^changeKnot/$', views.changeKnot, name='changeKnot'),
    url(r'^writeOrderToExcel/$', views.writeOrderToExcel, name='writeOrderToExcel'),
]