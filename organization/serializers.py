from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User

class OrganizationSerializer(ModelSerializer):
    class Meta:
        model=Organization
        fields = '__all__'


class ProcedureSerializer(ModelSerializer):
    class Meta:
        model=Procedure
        fields = '__all__'


class PracticeSerializer(ModelSerializer):
    class Meta:
        model=Practice
        fields = '__all__'



class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        # fields = '__all__'
        fields = ['first_name','last_name','password','email','username']