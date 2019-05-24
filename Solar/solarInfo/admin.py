from django.contrib import admin
from solarInfo import models
# Register your models here.


class NewSolarAdmin(admin.ModelAdmin):
    list_display = ['number', 's_voltage', 's_current', 'b_voltage', 'charging_status',
                    'load_current', 'load_voltage', 'lamp_status', 'work_time',
                    'cumulative_power', 'c_time']
    list_filter = ['number']


admin.site.register(models.Solar, NewSolarAdmin)
