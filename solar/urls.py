from django.urls import path
from solar import views


app_name = 'solar'


urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/solar/', views.ReturnSolar.as_view(), name='apisolar'),
    path('index/', views.index, name='index'),
    # path('detail/<int:solar_id>/', views.detail, name='detail'),
    # path('', views.dashboard),
]