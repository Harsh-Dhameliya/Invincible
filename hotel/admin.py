from django.contrib import admin
from hotel.models import Hotel

class HotelAdmin(admin.ModelAdmin):
    list_display  =("h_name",)


admin.site.register(Hotel,HotelAdmin)
