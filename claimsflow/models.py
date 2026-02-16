from django.db import models
from time import timezone


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract=True
        ordering=['-created_at']
    def __str__(self):
        return f'Created at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}'