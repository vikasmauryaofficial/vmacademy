from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import  Contact


# Create your views here.
def main_home(request):
   
    return render(request,'home/basic.html')


def about(request):
    return render(request, 'home/about.html')


def logout(request):
    return render(request,'home/logout.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'home/contact.html', {'thank': thank})