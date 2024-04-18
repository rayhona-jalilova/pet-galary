from django.db import models
from common.models.abstract import BaseModel
from .animal import Animal


class AnimalPhoto(BaseModel):
    animal_name = models.ForeignKey(Animal, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='animal_photos/')
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name