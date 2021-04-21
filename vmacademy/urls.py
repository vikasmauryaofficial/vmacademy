"""ftech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from user import views as user_view 
from django.contrib.auth import views as auth 
from login import views as vi
from user import views as vy
from . import views
from home import views as v

  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('login/',include('login.urls')),
    path('user/',include('user.urls')),
    path('form/', include('form.urls')),
    path('logout/',include('logout.urls')),

    
    
    path('',views.m_index, name="login"),

    path('',v.main_home),
    path('',vi.user_login),
    path('',vy.user_register,name="register"),
    
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+static(setting.MEDIA_URL,document_root=setting.MEDIA_ROOT)
