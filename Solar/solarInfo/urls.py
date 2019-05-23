# -*- coding:utf-8 -*-
__author__ = 'Bicycle'

from django.urls import path
from solarInfo import views


app_name = 'solarInfo'


urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/<int:number>/', views.dashboard, name='dashboard'),
    path('api/solar/', views.ReturnSolar.as_view(), name='apisolar'),
    path('index/', views.index, name='index'),
    # path('detail/<int:solar_id>/', views.detail, name='detail'),
    # path('', views.dashboard),
]