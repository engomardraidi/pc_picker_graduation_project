from django.urls import path
from . import views

urlpatterns = [
    path('motherboards/', views.MotherboardListView.as_view(), name='motherboards'),
]
