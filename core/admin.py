from django.contrib import admin
from .models import RegModel

@admin.register(RegModel)
class RegRegistration(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'phone')
