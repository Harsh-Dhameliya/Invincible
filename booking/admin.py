from django.contrib import admin
from booking.models import Bookings

class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","customer_id","name","mobile_no","birth_date","gender")

admin.site.register(Bookings,BookingAdmin)

