from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "book_id",
        "status",
        "created",
        "updated",
    )
    list_filter = ("created",)
    search_fields = (
        "book_id",
        "status",
        "title",
    )
    readonly_fields = ('book_id',)
