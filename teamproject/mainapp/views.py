from django.views.generic.base import TemplateView
from django.shortcuts import render

def mainpage(request):
    return render(request, '/dogapp/mainpage.html')