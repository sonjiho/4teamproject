from django.urls import path
from .views import *

app_name='mainapp'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('sort_m1_1/', sort_m1_1, name='sort_m1_1'),
    path('sort_m1_2/', sort_m1_2, name='sort_m1_2'),
    path('sort_m1_3/', sort_m1_3, name='sort_m1_3'),
    path('sort_m1_4/', sort_m1_4, name='sort_m1_4'),
    path('sort_m1_5/', sort_m1_5, name='sort_m1_5'),
    path('sort_r2/', sort_r2, name='sort_r2'),
    path('sort_m2_1/', sort_m2_1, name='sort_m2_1'),
    path('sort_m2_2/', sort_m2_2, name='sort_m2_2'),
    path('sort_m2_3/', sort_m2_3, name='sort_m2_3'),
    path('sort_end/', sort_end, name='sort_end'),
    path('sort_end_hu/', sort_end_hu, name='sort_end_hu')
]
