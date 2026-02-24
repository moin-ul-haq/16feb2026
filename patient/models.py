from django.db import models
from claimsflow.models import BaseModel
# from payment.models import Payment
from organization .models import *
# Create your models here.


# class Student(AbstractUser):
#     result = models.IntegerField()


#     def __str__(self):
#         return self.first_name
    







class Patient(BaseModel):
    # user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient_user',null=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,blank=True,null=True)
    age=models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='patient')
    practice = models.ForeignKey(Practice,on_delete=models.CASCADE,related_name='patient',null=True,blank=True)
    


    def __str__(self):
        return self.name
    


# class Claim(BaseModel):
#     choice=[
#         ('pending','Pending'),
#         ('successfull','Successfull'),
#     ]
#     # choice=[
#     #     'Pending',
#     #     'Successfully'
#     # ]
#     patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
#     procedures=models.ManyToManyField(Procedure, related_name='claim_procedures')
#     status=models.CharField(choices=choice,max_length=50)
#     total_price=models.IntegerField(blank=True,null=True)

#     def __str__(self):
#         return self.patient.user.first_name +' '+ str(self.id)
    
    # def save(self):
    #     a=Payment.objects.create(patient=self.patient,procedures=self.procedures,status='p')
    #     a.save()

    # def save(self, *args, **kwargs):
    #     procedures=self.procedures.all()
    #     total_cost=0
    #     for i in procedures:
    #         total_cost+=i.cost
    #     self.total_price=total_cost
    #     super().save(*args,**kwargs)