from rest_framework import serializers
from .models import *


# class ClaimSerializer(serializers.ModelSerializer):
#     practice_name = serializers.StringRelatedField(source = 'practice.name')
#     procedures_name = serializers.StringRelatedField(many=True,source='procedures')
#     patient_name = serializers.StringRelatedField(source='patient.name')
#     procedures = serializers.PrimaryKeyRelatedField(many=True,queryset=Procedure.objects.all())
#     class Meta:
#         model=Claim
#         fields = ['id','patient','practice','procedures','patient_name','practice_name','procedures_name','status','total_amount']


class ClaimSerializer(serializers.ModelSerializer):
    # practice_name = serializers.StringRelatedField(source = 'practice.name')
    procedures=serializers.PrimaryKeyRelatedField(many=True,queryset=Procedure.objects.all())
    procedures_name = serializers.StringRelatedField(many=True,source='procedures',read_only = True)
    # patient_name = serializers.StringRelatedField(source='patient.name')
    # procedures = serializers.PrimaryKeyRelatedField(many=True,queryset=Procedure.objects.all())
    class Meta:
        model=Claim
        fields = ['id','patient','practice','procedures','procedures_name','status','total_amount']
