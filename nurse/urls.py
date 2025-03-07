"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from nurse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('medical/', views.medical, name='medical'),
    path('nurselist/', views.nurselist, name='nurselist'),
    path('medicalrecordlist/', views.medicalrecordlist, name='medicalrecordlist'),
    path('editnurse/<int:id>/', views.editnurse, name='editnurse'),
    path('deletenurse/<int:id>/', views.deletenurse, name='deletenurse'),
    path('editmedicalrecord/<int:id>/', views.editmedicalrecord, name='editmedicalrecord'),
    path('deletemedicalrecord/<int:id>/', views.deletemedicalrecord, name='deletemedicalrecord'),
    path('nurseapi/', views.nurseapi, name='nurseapi'),
    path('medicalrecordapi/', views.medicalrecordapi, name='medicalrecordapi'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_update/<int:id>/', views.student_update, name='student_update'),
    path('student_delete/<int:id>/', views.student_delete, name='student_delete'),
]
