from django.contrib import admin

from .models import Reading
from .models import Config


class ReadingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Values', {'fields': ['instant', 'temp_val', 'humid_val']}),
        ('States', {'fields': ['temp_state', 'humid_state', 'light_state']}),
    ]

    readonly_fields = ('instant', 'temp_val', 'humid_val', 'temp_state', 'humid_state', 'light_state')


class ConfigAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Values', {'fields': ['temp_low', 'temp_high', 'humid_low', 'humid_high', 'hour_morning', 'hour_night']}),
        ('States', {'fields': ['temp_state', 'humid_state', 'light_state']}),
        ('Pins', {'fields': ['temp_humid_sensor', 'temp_pin', 'humid_pin', 'light_pin']}),
    ]

    readonly_fields = ('instant', )

admin.site.register(Reading, ReadingAdmin)
admin.site.register(Config, ConfigAdmin)
