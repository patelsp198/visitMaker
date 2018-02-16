from django.conf.urls import url, include
from reservHome import views

urlpatterns = [
	url(r'^$', views.index, name ='reservations.html'),
	url(r'^addReserv/', include('addReserv.urls')),
]