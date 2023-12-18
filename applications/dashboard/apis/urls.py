from django.urls import path
from . import views

urlpatterns = [
    path('motherboards/', views.MotherboardListView.as_view(), name='list-motherboards'),
    path('motherboards/<int:pk>/', views.SingleMotherboardView.as_view(), name='single-motherboard'),
]
