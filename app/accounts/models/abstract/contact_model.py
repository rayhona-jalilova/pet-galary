from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.abstract import BaseModel


class Contact(BaseModel):
    phone_number = models.CharField(_("Phone number"), max_length=14)
    email = models.EmailField(_("Email"), null=True, blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.phone_number}"
