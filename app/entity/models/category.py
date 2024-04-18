from  django.db import models
from common.models.abstract import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name