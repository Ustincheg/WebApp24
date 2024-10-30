from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static
import Users.views
from core.api.views import SubjetListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FilmView.as_view(), name = 'home'),
    path("<int:kinopoisk_id>/", views.film, name = 'film'),
    path('search/', views.Search.as_view(), name = 'search'),
    path('filter/', views.Filtr, name = 'filter'),
    path('login', Users.views.user_login, name = 'login-main'),
    path('logout', Users.views.user_logout, name = 'logout-main'),
    path('register', Users.views.user_register, name = 'register'), 
    path('confirm-email/<uuid:token>', Users.views.confirm_email, name='confirm-email'),
    path('api/', include('core.api.urls'))

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root = settings.MEDIA_ROOT)