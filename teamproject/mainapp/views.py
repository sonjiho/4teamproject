from django.views.generic.base import TemplateView
from django.shortcuts import render

def mainpage(request):
    return render(request, 'dogapp/sort_r1.html')


def sort_m1_1(request):
    return render(request, 'dogapp/sort_m1_1.html')


def sort_m1_2(request):
    return render(request, 'dogapp/sort_m1_2.html')


def sort_m1_3(request):
    return render(request, 'dogapp/sort_m1_3.html')


def sort_m1_4(request):
    return render(request, 'dogapp/sort_m1_4.html')


def sort_m1_5(request):
    return render(request, 'dogapp/sort_m1_5.html')


def sort_r2(request):
    return render(request, 'dogapp/sort_r2.html')


def sort_m2(request):
    return render(request, 'dogapp/sort_m2.html')