from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.abstract import BaseModel


class Address(BaseModel):
    street = models.CharField(_("Street"), max_length=254)
    city = models.CharField(_("City"), max_length=254)
    province = models.CharField(_("Province"), max_length=254)
    country = models.CharField(_("Country"), max_length=254)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} | {self.city}"
