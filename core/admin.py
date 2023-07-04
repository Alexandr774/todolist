from django.contrib import admin
from .models import User

@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")
    search_fields = ("username", "last_name",)
    list_filter = ("is_superuser", "is_staff", "is_active")
    exclude = ["password"]
    readonly_fields = ("date_joined", "last_login")

