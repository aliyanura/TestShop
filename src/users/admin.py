from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser",
                     "is_active", "is_deleted")
    list_display_links = ("username", "email")
    list_filter = ("is_active", "is_staff", "is_deleted",
                   "is_superuser", "created_at")
    readonly_fields = ("created_at", "updated_at", "last_login")
    search_fields = ("username", "email")
    ordering = ('-created_at',)
    list_per_page = 25
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "full_name",
                    "lombard",
                    "is_superuser",
                    "is_staff",
                    "is_admin",
                    "is_employee",
                    "is_active",
                    "is_deleted",
                    "created_at",
                    "updated_at",
                    "last_login",
                )
            },
        ),
    )
