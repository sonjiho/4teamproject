from django.urls import path
from .views import *

app_name='mainapp'

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
]