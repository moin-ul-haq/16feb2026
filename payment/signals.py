from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Payment


@receiver(post_save,sender=Payment)
def update_claim_status(instance,created,sender,**kwargs):
    # print('-----------------------------------------')
    if created:
        # print('--------------pass-------------------')
        pass
    else:
        # print('------------------run--------------------')
        claim = instance.claim
        if instance.status == 'completed':
            # print('-----Entered---')
            claim.status = 'successfull'
            claim.save(update_fields=["status"])
        elif instance.status == 'pending':
            claim.status = 'pending'
            claim.save(update_fields=["status"])