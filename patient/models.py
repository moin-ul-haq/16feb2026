from django.db import models
from claimsflow.models import BaseModel
# from payment.models import Payment
from organization .models import *
from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser, User

# Create your models here.



class Patient(BaseModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient_user',null=True)
    # name=models.CharField(max_length=50)
    # email=models.EmailField(max_length=50,default='moinakf@gmail.com')
    # # age=models.IntegerField()
    # phone = models.CharField(max_length=15, null=True, blank=True)
    # address = models.TextField(null=True, blank=True)
    # practice = models.ForeignKey(Practice,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.user.first_name
    


class Claim(BaseModel):
    choice=[
        ('p','Pending'),
        ('s','Successfully'),
    ]
    # choice=[
    #     'Pending',
    #     'Successfully'
    # ]
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    procedures=models.ManyToManyField(Procedure, related_name='claim_procedures')
    status=models.CharField(choices=choice,max_length=50)

    def __str__(self):
        return self.patient.user.first_name +' '+ str(self.id)
    
    # def save(self):
    #     a=Payment.objects.create(patient=self.patient,procedures=self.procedures,status='p')
    #     a.save()