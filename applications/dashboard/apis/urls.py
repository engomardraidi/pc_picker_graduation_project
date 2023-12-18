from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cpus', views.CPUViewSet, basename='cpus')

urlpatterns = [
    path('motherboards/', views.MotherboardListView.as_view(), name='list-motherboards'),
    path('motherboards/<int:pk>/', views.SingleMotherboardView.as_view(), name='single-motherboard'),
]

urlpatterns += router.urls