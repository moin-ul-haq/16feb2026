from rest_framework import serializers
from .models import *

class PaymentSerializer(serializers.ModelSerializer):
    # claim = serializers.StringRelatedField()
    practice = serializers.StringRelatedField(source = 'claim.practice')
    patient = serializers.StringRelatedField(source = 'claim.patient')
    class Meta:
        model=Payment
        fields = ['id','patient','amount','claim','practice','status']
