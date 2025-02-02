from django.contrib import admin
from transportation.models import Transportation

class TransportationAdmin(admin.ModelAdmin):
    list_display  =("t_name",)

admin.site.register(Transportation,TransportationAdmin)