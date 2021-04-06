from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin,
)

from users.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("email", "date_joined", "is_active")
    list_filter = ("date_joined", "is_active", "is_staff")

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
