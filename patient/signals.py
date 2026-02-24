# from django.db.models.signals import m2m_changed,post_save
# from django.dispatch import receiver
# from patient.models import Claim
# from payment.models import Payment



# @receiver(m2m_changed, sender=Claim.procedures.through)
# def generate_total_price(sender, instance, action, **kwargs):
#     # print('heloo------------')
#     if action in ["post_add", "post_remove", "post_clear"]:

#         total_price = sum(
#             procedure.cost for procedure in instance.procedures.all()
#         )

#         instance.total_price = total_price
#         # print(instance.total_price)
#         instance.save(update_fields=["total_price"])

#         Payment.objects.update_or_create(
#         claim=instance,
#         defaults={
#             "amount": total_price,
#             "status": "pending"
#         }
#     )        


# # @receiver(post_save,sender=Claim.procedures.through) 
# # def generate_total_price(sender, instance,created, **kwargs): 
# #     print('Hello')
# #     if created: 
# #         procedures=instance.procedures.all() 
# #         total_price=0 
# #         for i in procedures: 
# #             total_price+=i.cost 
# #         instance.total_price=total_price 
# #         instance.save()



# # @receiver(post_save,sender=Claim)
# # def create_payment(sender,instance,created,**kwargs):
# #     print('heloo------')
# #     if created:
# #         a=Payment.objects.create(claim=instance,status='pending', amount=instance.total_price)
# #         print(instance.total_price)

# #         a.save()