from django.contrib import admin

from .models import Genre, Films, Country, Watch_later, Comments

admin.site.register(Genre)
admin.site.register(Films)
admin.site.register(Country)
admin.site.register(Watch_later)
admin.site.register(Comments)