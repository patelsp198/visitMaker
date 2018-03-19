from django.conf.urls import url, include
from addReserv import views

urlpatterns = [
	url(r'^$', views.get_name, name ='addReserv.html'),
  	url(r'^confirmReserv/', include('confirmReserv.urls')),
]