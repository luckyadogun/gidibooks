from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import User
from users.forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm

    list_display = ("email", "date_joined", "is_active")
    list_filter = ("date_joined", "is_active", "is_staff")

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()

    readonly_fields = ("user_id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "user_id",
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )


admin.site.unregister(Group)
