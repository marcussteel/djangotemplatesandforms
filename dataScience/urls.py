from urllib import request
from django.urls import path,include
from .views import homeds

urlpatterns = [
    path('',homeds,name='homeds')
]