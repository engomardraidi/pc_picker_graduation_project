from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'motherboards', views.MotherboardViewSet, basename='motherboards')
router.register(r'cpus', views.CPUViewSet, basename='cpus')

urlpatterns = router.urls