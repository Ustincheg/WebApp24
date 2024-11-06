from django.contrib import admin
from .models import Profile, EmailToken
# Register your models here.
admin.site.register(Profile)
admin.site.register(EmailToken)