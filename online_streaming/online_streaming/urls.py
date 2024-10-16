from django.contrib import admin
from django.urls import path
from core import views
import Users.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FilmView.as_view(), name = 'home'),
    path("<int:kinopoisk_id>/", views.film, name = 'film'),
    path('search/', views.Search.as_view(), name = 'search'),
    path('filter/', views.Filtr, name = 'filter'),
    path('login', Users.views.user_login, name = 'login'),
    path('logout', Users.views.user_logout, name = 'logout'),
    path('register', Users.views.user_register, name = 'register'), 
    path('confirm-email/<uuid:token>', Users.views.confirm_email, name='confirm-email'),

    
]
