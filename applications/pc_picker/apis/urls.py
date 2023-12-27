from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.ListOfDevices.as_view(), name='devices'),
    path('fields/', views.ListOfFields.as_view(), name='fields'),
    path('pick-pc/', views.pick_pc, name='pick-pc'),
    path('pick-cpus/', views.pick_cpus, name='pick-cpus'),
    path('pick-rams/', views.pick_rams, name='pick-rams'),
    path('pick-gpus/', views.pick_gpus, name='pick-gpus'),
    path('pick-cases/', views.pick_cases, name='pick-cases'),
]
