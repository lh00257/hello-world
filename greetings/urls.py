from django.conf.urls import url  #import built in url function

from .views import index  #import index view


urlpatterns = [
    url(r'^$', index),  #r' indicates a rw string, lnkd to index 
]                       
	
