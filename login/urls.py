from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'login' 
urlpatterns = [
    url('', views.user_login, name='user_login'),
   
    
   
]