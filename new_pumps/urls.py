from django.urls import path
from . import views

urlpatterns = [
    path('', views.pump_list, name='pump_list'),
    path('nozzles/', views.nozzle_list, name='nozzle_list'),
    path('sales/', views.sale_list, name='sale_list'),
]
