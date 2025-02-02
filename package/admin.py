from django.contrib import admin
from django.utils.html import strip_tags
from package.models import Package

class PackageAdmin(admin.ModelAdmin):

    
    list_display = ("Package_name","Package_price","Total_days","Total_nights","Package_description","category","Transportation_type","Guid_name","Hotel_name","Package_image1","Package_image2","Package_image3")



# def short_description(self, obj):
#     return strip_tags(obj.Package_description)[:50] + "..." if obj.p_description else "No Description"

# short_description("Package_description")

admin.site.register(Package,PackageAdmin)
