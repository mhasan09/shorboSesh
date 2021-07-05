from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(NEWS)
class NEWS_ADMIN(admin.ModelAdmin):
    list_display = [f.name for f in NEWS._meta.fields]