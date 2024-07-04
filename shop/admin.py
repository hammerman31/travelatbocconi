# shop/admin.py
from django.contrib import admin
from .models import Trip, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1  # Number of extra empty option fields to display

class TripAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Trip, TripAdmin)
