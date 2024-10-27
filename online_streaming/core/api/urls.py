from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('subjects/', views.SubjetListView.as_view()),
    path('subjects/<int:pk>', views.SubjectDetailView.as_view()),
    path('subjects/create', views.SubjectCreateView.as_view()),
    path('subjects/update/<int:pk>', views.SubjectUpdateView.as_view()),
    path('auth/', include('djoser.urls')), 
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

