from django.urls import path
from . import views

urlpatterns = [
    path('pick_pc/', views.pick_pc, name='test')
]
