from django.contrib import admin
from guide.models import Guide

class GuideAdmin(admin.ModelAdmin):
    list_display =("g_name","g_lang","g_experience")



admin.site.register(Guide,GuideAdmin)