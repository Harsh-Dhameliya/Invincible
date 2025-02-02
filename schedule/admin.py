from django.contrib import admin
from schedule.models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('start_date','end_date','total_days')


admin.site.register(Schedule,ScheduleAdmin)
