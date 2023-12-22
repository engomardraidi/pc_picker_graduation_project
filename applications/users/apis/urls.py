from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('tokens/refresh/', views.refresh_token_view, name='refresh'),
    path('<int:pk>/', views.user_account, name='user-account'),
    path('new/', views.new_user, name='new-user'),
    path('delete/', views.delete_user, name='delete-user'),
    path('list/', views.ListUsers.as_view(), name='users-list')
]
