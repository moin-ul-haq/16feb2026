from django.db import models
from claimsflow.models import BaseModel
from patient.models import Patient
from organization.models import Procedure,Practice

# Create your models here.
class Claim(BaseModel):
    choice=[
        ('pending','Pending'),
        ('successfull','Successfull'),
    ]
    # choice=[
    #     'Pending',
    #     'Successfully'
    # ]
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE,related_name='claim')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    procedures=models.ManyToManyField(Procedure, related_name='claim_procedures')
    status=models.CharField(choices=choice,max_length=50)
    total_amount=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.patient.name +' '+ str(self.id)