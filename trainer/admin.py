from django.contrib import admin
from .models import SQLTask
from .models import HistoricalEvent

admin.site.register(HistoricalEvent)
admin.site.register(SQLTask)
