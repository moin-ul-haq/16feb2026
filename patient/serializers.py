from rest_framework.serializers import ModelSerializer
from .models import *


class ClaimSerializer(ModelSerializer):
    class Meta:
        model=Claim
        fields = '__all__'
