from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmView.as_view(), name = "home"),
    path('search/', views.Search.as_view(), name='search'), 
    path('filter/', views.Filtr, name='filter'),
    path('search_navbar/', views.search_navbar, name = 'search_navbar'),
    path('films/<int:kinopoisk_id>/', views.film, name = 'film'),
    path('watch-later/<int:kinopoisk_id>/', views.watch_later, name = 'watch_later'),
    path('films-watch/', views.Film_watch , name='films-watch'),
    path('add-comment/<int:kinopoisk_id>/', views.add_comment, name='add_comment'),
    path('remove-comment/<int:kinopoisk_id>/<int:comment_id>',  views.remove_comment, name='remove_comment')

] 