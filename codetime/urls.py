from django.conf.urls import url
from . import views
app_name = 'codetime'
urlpatterns = [
    url(r'^jtbq/$', views.jtbq, name='jtbq'),
    url(r'^code/$', views.code, name='code'),
    url(r'^login/$', views.loginForm, name='loginForm'),
    url(r'^product/(?P<item_id>\d+)$', views.product, name='product'),
    url(r'^productForm/$', views.productForm, name='productForm'),
    url(r'^orderSearch/$', views.orderSearch, name='orderSearch'),
    url(r'^changeShipments/$', views.changeShipments, name='changeShipments'),
    url(r'^changeStatus/$', views.changeStatus, name='changeStatus'),
    url(r'^changeKnot/$', views.changeKnot, name='changeKnot'),
    url(r'^writeOrderToExcel/$', views.writeOrderToExcel, name='writeOrderToExcel'),
]