from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "show_on_homepage")
    list_editable = ("show_on_homepage",)
    search_fields = ("name", "title")
