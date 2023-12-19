from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'motherboards', views.MotherboardViewSet, basename='motherboards')
router.register(r'cpus', views.CPUViewSet, basename='cpus')
router.register(r'rams', views.RAMViewSet, basename='rams')

urlpatterns = router.urls