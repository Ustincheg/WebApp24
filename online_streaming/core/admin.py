from django.contrib import admin

from .models import Genre, Films, Country

admin.site.register(Genre)
admin.site.register(Films)
admin.site.register(Country)