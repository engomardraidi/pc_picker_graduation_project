from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
