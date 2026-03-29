"""Admin configuration for SQL Trainer application."""
from django.contrib import admin

from .models import HistoricalEvent, SQLTask

admin.site.register(HistoricalEvent)
admin.site.register(SQLTask)

