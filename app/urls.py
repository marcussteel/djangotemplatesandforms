"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import home, homefs, student_delete, student_detail, student_list,student_add, student_update
from django.urls import path,include



urlpatterns = [
    path('',home, name='home'),
    path('main',homefs, name='homefs'),
    path('list/', student_list, name='list'),
    path('add/', student_add, name='add'),
    path('update/<int:id>', student_update, name='update'),
    path('delete/<int:id>', student_delete, name='delete'),
    path('detail/<int:id>', student_detail, name="detail"),
  
]