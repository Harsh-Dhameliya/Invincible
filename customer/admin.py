from django.contrib import admin
from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","customer_name","customer_email","customer_mobile","password")

admin.site.register(Customer , CustomerAdmin)