from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_home, name="main_home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("logout/", views.logout, name="logout"),
    
]
