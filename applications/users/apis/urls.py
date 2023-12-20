from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.user_account, name='user-account'),
    path('users/new/', views.new_user, name='new-user'),
]
