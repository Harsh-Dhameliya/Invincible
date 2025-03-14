from django.contrib import admin
from django.utils.html import strip_tags
from package.models import Package,Schedule


class ScheduleInline(admin.StackedInline):  
    model = Schedule  
    extra = 1  # Show at least one empty form  
    ordering = ['day_number']  # Sort by day number

class PackageAdmin(admin.ModelAdmin):

    
    list_display = ("Package_name","Package_price","Total_days","Total_nights","start_date","end_date","Package_description","category","Transportation_type","Guid_name","Hotel_name","Package_image1","Package_image2","Package_image3")

    inlines = [ScheduleInline]  # Attach the inline form  

    def schedule_summary(self, obj):  
        """Display a summary of the schedule in the Package list view."""  
        return ", ".join([f"Day {s.day_number}: {s.activity[:20]}: {s.activity_description[:20]}:{s.date}..." for s in obj.schedules.all()])  

    schedule_summary.short_description = "Schedule Overview" 

    class Media:
        js = ('admin/js/custom_admin.js','admin/js/custom_shedual.js')


# def short_description(self, obj):
#     return strip_tags(obj.Package_description)[:50] + "..." if obj.p_description else "No Description"

# short_description("Package_description")

admin.site.register(Package,PackageAdmin)
