from django.shortcuts import render
from .models import Dogplace
from django.db.models import Avg


def mainpage(request):
    return render(request, 'dogapp/sort_r1.html')


def sort_m1_1(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        category_id = request.GET.get('category_id', "")
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id': category_id
        }
    return render(request, 'dogapp/sort_m1_1.html', context)


def sort_m1_2(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        category_id = request.GET.get('category_id', "")
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id': category_id
        }
    return render(request, 'dogapp/sort_m1_2.html', context)


def sort_m1_3(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        category_id = request.GET.get('category_id', "")
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id': category_id
        }
    return render(request, 'dogapp/sort_m1_3.html', context)


def sort_m1_4(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        category_id = request.GET.get('category_id', "")
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id': category_id
        }
    return render(request, 'dogapp/sort_m1_4.html', context)


def sort_m1_5(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        category_id = request.GET.get('category_id', "")
        context = {
            'results': {
                'result_r1': (result_r1 + " > ")
            },
            'category_id': category_id
        }
    return render(request, 'dogapp/sort_m1_5.html', context)


def sort_r2(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        result_m1 = request.GET.getlist("result_m1", "")
        category_id = request.GET.get('category_id', "")
        type_id = request.GET.getlist('type_id', "")
        context = {
            'results': {
                'result_r1': result_r1,
                'result_m1': (result_m1[0] + " 외 " + str(len(result_m1) - 1) + "개 > "),
            },
            'category_id': category_id,
            'type_id': type_id
        }
    return render(request, 'dogapp/sort_r2.html', context)


def sort_m2_1(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        result_m1 = request.GET.get("result_m1", "")
        result_r2 = request.GET.get('result_r2', "")
        category_id = request.GET.get('category_id', "")
        type_id = request.GET.getlist('type_id', "")
        state_id = request.GET.get('state_id', "")
        context = {
            'results': {
                'result_r1': result_r1,
                'result_m1': result_m1,
                'result_r2': (result_r2 + " > ")
            },
            'category_id': category_id,
            'type_id': type_id,
            'state_id': state_id
        }
    return render(request, 'dogapp/sort_m2_1.html', context)


def sort_m2_2(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        result_m1 = request.GET.get("result_m1", "")
        result_r2 = request.GET.get('result_r2', "")
        category_id = request.GET.get('category_id', "")
        type_id = request.GET.getlist('type_id', "")
        state_id = request.GET.get('state_id', "")
        context = {
            'results': {
                'result_r1': result_r1,
                'result_m1': result_m1,
                'result_r2': (result_r2 + " > ")
            },
            'category_id': category_id,
            'type_id': type_id,
            'state_id': state_id
        }
    return render(request, 'dogapp/sort_m2_2.html', context)


def sort_m2_3(request):
    context = ""
    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        result_m1 = request.GET.get("result_m1", "")
        result_r2 = request.GET.get('result_r2', "")
        category_id = request.GET.get('category_id', "")
        type_id = request.GET.getlist('type_id', "")
        state_id = request.GET.get('state_id', "")
        context = {
            'results': {
                'result_r1': result_r1,
                'result_m1': result_m1,
                'result_r2': (result_r2 + " > ")
            },
            'category_id': category_id,
            'type_id': type_id,
            'state_id': state_id
        }
    return render(request, 'dogapp/sort_m2_3.html', context)


def sort_end(request):

    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        result_m1 = request.GET.get("result_m1", "")
        result_r2 = request.GET.get('result_r2', "")
        result_m2 = request.GET.getlist("result_m2", "")
        type_id = request.GET.getlist('type_id', "")
        city_id = request.GET.getlist('city_id', "")
        total_result = Dogplace.objects.filter(city_id__in=city_id) & Dogplace.objects.filter(type_id__in=type_id)
        len_result = len(total_result)
        avg_lat = total_result.aggregate(Avg('lat'))
        avg_lng = total_result.aggregate(Avg('lon'))
        context = {
            'results': {
                'result_r1': result_r1,
                'result_m1': result_m1,
                'result_r2': result_r2,
                'result_m2': (result_m2[0] + " 외 " + str(len(result_m2) - 1) + "개"),
            },
            'type_id': type_id,
            'city_id': city_id,
            'total_result': total_result,
            'len_result': len_result,
            'avg_lat': avg_lat["lat__avg"],
            'avg_lng': avg_lng["lon__avg"]
        }
    return render(request, 'dogapp/sort_end.html', context)


def sort_end_hu(request):

    if request.method == 'GET':
        result_r1 = request.GET.get('result_r1', "")
        total_result = Dogplace.objects.filter(type_id="29")
        len_result = len(total_result)
        avg_lat = total_result.aggregate(Avg('lat'))
        avg_lng = total_result.aggregate(Avg('lon'))

        context = {
            'results': {
                'result_r1': result_r1
            },
            'total_result': total_result,
            'len_result': len_result,
            'avg_lat': avg_lat["lat__avg"],
            'avg_lng': avg_lng["lon__avg"]
        }
    return render(request, 'dogapp/sort_end_hu.html', context)
