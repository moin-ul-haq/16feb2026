from claimsflow.models import BaseModel
from django.db import models

# Create your models here.

class Organization(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Practice(BaseModel):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.name
    

class Procedure(BaseModel):
    name=models.CharField(max_length=50)
    cost=models.IntegerField()
    practice = models.ForeignKey(Practice,on_delete=models.CASCADE,related_name='procedure')


    def __str__(self):
        return self.name
    


