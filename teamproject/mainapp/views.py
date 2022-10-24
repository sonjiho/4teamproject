import os
import csv
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Dogplace


def mainpage(request):
    return render(request, 'dogapp/sort_r1.html')


def sort_m1_1(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        category_id = request.GET.get('category_id')
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id':category_id
        }
    return render(request, 'dogapp/sort_m1_1.html', context)


def sort_m1_2(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        category_id = request.GET.get('category_id')
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id':category_id
        }
    return render(request, 'dogapp/sort_m1_2.html', context)


def sort_m1_3(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        category_id = request.GET.get('category_id')
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id':category_id
        }
    return render(request, 'dogapp/sort_m1_3.html', context)


def sort_m1_4(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        category_id = request.GET.get('category_id')
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id':category_id
        }
    return render(request, 'dogapp/sort_m1_4.html', context)

def sort_m1_5(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        category_id = request.GET.get('category_id')
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id':category_id
        }
    return render(request, 'dogapp/sort_m1_5.html', context)


def sort_r2(request):
    context=""
    type_ids=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1","")
        category_id = request.GET.get('category_id')
        type_id = request.GET.getlist('type_id')
        for f  in type_id:
            type_ids += f
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': (result_m1 [0] + " 외 " + str(len(result_m1)-1) + "개 > "),
            },
            'category_id':category_id,
            'type_id': type_ids
        }
    return render(request, 'dogapp/sort_r2.html', context)


def sort_m2_1(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        category_id = request.GET.get('category_id')
        type_id = request.GET.get('type_id')
        state_id = request.GET.get('state_id')
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1 ,
                'result_r2': (result_r2+ " > ")
            },
            'category_id':category_id,
            'type_id': type_id,
            'state_id': state_id
        }
    return render(request, 'dogapp/sort_m2_1.html', context)


def sort_m2_2(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        category_id = request.GET.get('category_id')
        type_id = request.GET.get('type_id')
        state_id = request.GET.get('state_id')
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1,
                'result_r2': (result_r2+ " > ")
            },
            'category_id':category_id,
            'type_id': type_id,
            'state_id': state_id
        }
    return render(request, 'dogapp/sort_m2_2.html', context)


def sort_m2_3(request):
    context=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        category_id = request.GET.get('category_id')
        type_id = request.GET.get('type_id')
        state_id = request.GET.get('state_id')
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1,
                'result_r2': (result_r2+ " > ")
            },
            'category_id':category_id,
            'type_id': type_id,
            'state_id': state_id
        }
    return render(request, 'dogapp/sort_m2_3.html', context)


def sort_end(request):
    context=""
    city_ids=""
    result_m2 = []
    if request.method == 'GET' and len(result_m2) > 0:
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.get("result_m1","")
        result_r2 = request.GET.get('result_r2',"")
        result_m2 = request.GET.getlist("result_m2","")
        category_id = request.GET.get('category_id')
        type_id = request.GET.get('type_id')
        state_id = request.GET.get('state_id')
        city_id = request.GET.getlist('city_id')
        for r in city_id:
            city_ids += r

        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1,
                'result_r2': result_r2,
                'result_m2': (result_m2 [0] + " 외 " + str(len(result_m2)-1) + "개")
            },
            'category_id':category_id,
            'type_id': type_id,
            'state_id': state_id,
            'city_id' : city_ids
        }

    else :
        result_r1 = request.GET.get('result_r1')
        category_id = request.GET.get('category_id')

        context = {
            'results': {
                'result_r1': result_r1
            },
            'category_id':category_id
        }
    return render(request, 'dogapp/sort_end.html', context)