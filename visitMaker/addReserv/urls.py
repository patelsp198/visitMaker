from django.conf.urls import url
from addReserv import views

urlpatterns = [
	url(r'^$', views.index, name ='addReserv.html'),
]