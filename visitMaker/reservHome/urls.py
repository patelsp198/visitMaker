from django.conf.urls import url
from reservHome import views

urlpatterns = [
	url(r'^$', views.index, name ='reservations.html'),
]