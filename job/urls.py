from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.job_list),
    path('<str:slug>', views.job_details, name='job_detail'),
]
