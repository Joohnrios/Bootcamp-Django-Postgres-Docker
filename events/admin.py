from django.contrib import admin
from events.models import Event
# Register your models here.

class AdminEvent(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'created_at')

admin.site.register(Event, AdminEvent)
