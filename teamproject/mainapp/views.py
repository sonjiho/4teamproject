import os
import csv
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render

def mainpage(request):
    return render(request, 'dogapp/sort_r1.html')


def sort_m1_1(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m1_1.html', context)


def sort_m1_2(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m1_2.html', context)


def sort_m1_3(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
        return render(request, 'dogapp/sort_m1_3.html', context)


def sort_m1_4(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m1_4.html', context)

def sort_m1_5(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m1_5.html', context)


def sort_r2(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_r2.html', context)


def sort_m2_1(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m2_1.html', context)


def sort_m2_2(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m2_2.html', context)


def sort_m2_3(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_m2_3.html', context)


def sort_end(request):
    context=""
    result_m1_1= ""
    result_m2_1=""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1',"")
        result_m1 = request.GET.getlist("result_m1 ","")
        for r in result_m1:
            result_m1_1 += r + " "
        result_r2=request.GET.get('result_r2',"")
        result_m2= request.GET.getlist("result_m2","")
        for f in result_m2:
            result_m2_1 += f+ " "
        context = {
            'results': {
                'result_r1': result_r1 ,
                'result_m1': result_m1_1 ,
                'result_r2': result_r2,
                'result_m2':result_m2_1 ,
            }
        }
    return render(request, 'dogapp/sort_end.html', context)