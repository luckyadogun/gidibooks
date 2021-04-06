import uuid

from django.db import models
from django.utils.translation import gettext as _

from users.models import User

BORROWED = "borrowed"
AVAILABLE = "available"
PENDING = "pending"


class Book(models.Model):
    BOOK_STATUS = (
        (BORROWED, BORROWED),
        (AVAILABLE, AVAILABLE),
        (PENDING, PENDING),
    )

    book_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(_("title"), max_length=200)
    borrower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    status = models.CharField(
        _("book status"),
        max_length=20,
        choices=BOOK_STATUS,
        default=AVAILABLE,
    )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_book_id(self):
        return str(self.book_id)

    def __str__(self):
        return self.title
