from django.contrib import admin
from review.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id","name" , "review",)

    def has_add_permission(self, request):
        return False

admin.site.register(Review,ReviewAdmin)

# Register your models here.
