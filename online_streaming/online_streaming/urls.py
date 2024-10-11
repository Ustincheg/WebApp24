from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FilmView.as_view()),
    path("<int:kinopoisk_id>/", views.film, name = 'film'),
    path('search/', views.Search.as_view(), name = 'search'),
    path('filter/', views.Filtr, name = 'filter'),
    
]
