from rest_framework.serializers import ModelSerializer
from .models import *


# class ClaimSerializer(ModelSerializer):
#     class Meta:
#         model=Claim
#         fields = '__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','name','email','age','organization','practice',]
