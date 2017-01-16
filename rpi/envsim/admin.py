from django.contrib import admin

from .models import Reading
from .models import Config


class ReadingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Values', {'fields': ['instant', 'temp_val', 'humid_val']}),
        ('States', {'fields': ['temp_state', 'humid_state', 'light_state']}),
    ]

    readonly_fields = ('instant', )


class ConfigAdmin(admin.ModelAdmin):
    fieldsets = [
        ('State', {'fields': ['temp_state', 'humid_state', 'light_state']})
    ]

    readonly_fields = ('instant', )

admin.site.register(Reading, ReadingAdmin)
admin.site.register(Config, ConfigAdmin)
