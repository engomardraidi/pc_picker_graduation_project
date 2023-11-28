from django.urls import path
from . import views

urlpatterns = [
    path('fields/', views.FieldView.as_view(), name='create-field'),
    path('pc-config/', views.pc_configuration, name='pc-config')
]
