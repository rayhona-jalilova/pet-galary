from django.db import models
from common.models.abstract import BaseModel
from accounts.models import Address, Contact

class Animal(BaseModel):
    name= models.CharField(max_length=124)
    address= models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    contact= models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Animal"
        verbose_name_plural = "Animals"

    def __str__(self) -> str:
        return f"{self.name}"
    