from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'logout' 
urlpatterns = [
    url('', views.logout, name='logout'),
   
    
   
]