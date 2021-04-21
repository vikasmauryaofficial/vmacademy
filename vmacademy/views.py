from django.shortcuts import render

from django.http import HttpResponse

def m_index(request):
    return render(request,'index.html')
