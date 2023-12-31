from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.ListOfDevices.as_view(), name='devices'),
    path('fields/', views.ListOfPCFields.as_view(), name='fields'),
    path('pick-laptop/', views.pick_laptop, name='pick-laptop'),
    path('pick-pc/', views.pick_pc, name='pick-pc'),
    path('pick-motherboards/', views.pick_motherboards, name='pick-motherboards'),
    path('pick-cpus/', views.pick_cpus, name='pick-cpus'),
    path('pick-rams/', views.pick_rams, name='pick-rams'),
    path('pick-gpus/', views.pick_gpus, name='pick-gpus'),
    path('pick-cases/', views.pick_cases, name='pick-cases'),
    path('pick-internal-drives/', views.pick_internal_drives, name='pick-internal-drives'),
    path('pick-power-supplies/', views.pick_power_supplies, name='pick-power-supplies'),
]
