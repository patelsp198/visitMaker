from django.conf.urls import url
from confirmReserv import views

urlpatterns = [
  url(r'^$', views.index, name ='confirmReserv.html'),
]