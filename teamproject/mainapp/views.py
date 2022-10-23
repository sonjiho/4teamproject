import os
import csv
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from mainapp.models import DMap
def mainpage(request):
    return render(request, 'dogapp/sort_r1.html')


def sort_m1_1(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        context = {
            'results': {
                'result_r1': (result_r1 + " > "),
            }
        }
    return render(request, 'dogapp/sort_m1_1.html', context)


def sort_m1_2(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        context = {
            'results': {
                'result_r1': (result_r1 + " > "),
            }
        }
    return render(request, 'dogapp/sort_m1_2.html', context)


def sort_m1_3(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        context = {
            'results': {
                'result_r1': (result_r1 + " > "),
            }
        }
    return render(request, 'dogapp/sort_m1_3.html', context)


def sort_m1_4(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        context = {
            'results': {
                'result_r1': (result_r1 + " > "),
            }
        }
    return render(request, 'dogapp/sort_m1_4.html', context)

def sort_m1_5(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        context = {
            'results': {
                'result_r1': (result_r1 + " > "),
            }
        }
    return render(request, 'dogapp/sort_m1_5.html', context)


def sort_r2(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1","")
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': (result_m1 [0] + " 외 " + str(len(result_m1)-1) + "개 > "),
            }
        }
    return render(request, 'dogapp/sort_r2.html', context)


def sort_m2_1(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1 ,
                'result_r2': (result_r2+ " > "),
            }
        }
    return render(request, 'dogapp/sort_m2_1.html', context)


def sort_m2_2(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1,
                'result_r2': (result_r2+ " > "),
            }
        }
    return render(request, 'dogapp/sort_m2_2.html', context)


def sort_m2_3(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1,
                'result_r2': (result_r2+ " > "),
            }
        }
    return render(request, 'dogapp/sort_m2_3.html', context)


def sort_end(request):
    context=""
    result_m2 = []
    if request.method == 'GET' and len(result_m2) > 0:
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        result_m2 = request.GET.getlist("result_m2","")

        DMap_1 = DMap.objects.filter(sub_class = '중식')
        DMap_1_length = len(DMap_1)
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1,
                'result_r2': result_r2,
                'result_m2': (result_m2 [0] + " 외 " + str(len(result_m2)-1) + "개")
            },
            'DMap_1': DMap_1,
            'DMap_1_length': DMap_1_length
        }
    else :
        result_r1 = request.GET.get('result_r1')
        DMap_1 = DMap.objects.filter(sub_class='중식')
        DMap_1_length = len(DMap_1)

        context = {
            'results': {
                'result_r1': result_r1 },
            'DMap_1': DMap_1,
            'DMap_1_length': DMap_1_length
            }
    return render(request, 'dogapp/sort_end.html', context)