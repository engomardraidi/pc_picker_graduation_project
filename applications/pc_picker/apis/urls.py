from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_expert_system, name='test')
]
