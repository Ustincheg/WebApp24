from django.urls  import path

from .views import * 

from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.user_login, name = 'login-main'),
    path('logout/', views.user_logout, name = 'logout-main'),
    path('register/', views.user_register, name = 'register'), 
    path('confirm-email/<uuid:token>/', views.confirm_email, name='confirm-email'),
    
]