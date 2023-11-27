from django.urls import path
from . import views

urlpatterns = [
    # path('fields/', views.FieldListView.as_view(), name='fields-list'),
    path('pc-config/', views.pc_configuration, name='pc-config')
]
