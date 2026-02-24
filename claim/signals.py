from django.db.models.signals import m2m_changed,post_save
from django.dispatch import receiver
from .models import Claim
from payment.models import Payment



@receiver(m2m_changed, sender=Claim.procedures.through)
def generate_total_price(sender, instance, action, **kwargs):
    # print('heloo------------')
    if action in ["post_add", "post_remove", "post_clear"]:

        total_price = sum(
            procedure.cost for procedure in instance.procedures.all()
        )

        instance.total_amount = total_price
        # print(instance.total_price)
        instance.save(update_fields=["total_amount"])

        Payment.objects.update_or_create(
        claim=instance,
        defaults={
            "amount": total_price,
            "status": "pending"
        }
    )        

