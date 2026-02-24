from django.db import models
from claimsflow.models import BaseModel
from claim.models import Claim
# Create your models here.


class Payment(BaseModel):
    choice=[
        ('pending','Pending'),
        ('completed','Completed')
        ]
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    amount= models.IntegerField()
    status = models.CharField(choices=choice,max_length=50)