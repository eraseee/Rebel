from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [ 
	url(r'^products/$', views.product_list),
	url(r'^products/(?P<pk>[0-9])/$', views.product_details),
	url(r'^products?company=(?P<pk>[0-9])/$', views.products_by_company),
	url(r'^products/(?P<pk>[0-9])/countries/$', views.product_countries),
]