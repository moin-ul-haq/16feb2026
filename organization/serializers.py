from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields = '__all__'


class ProcedureSerializer(serializers.ModelSerializer):
    # practice = serializers.PrimaryKeyRelatedField(queryset = Practice.objects.all())
    practice_name = serializers.StringRelatedField(source = 'practice.name')
    organization = serializers.StringRelatedField(source = 'practice.organization.name')
    class Meta:
        model=Procedure
        fields = ['id','name','cost','practice','practice_name','organization']
        # fields = '__all__'



class PracticeSerializer(serializers.ModelSerializer):
    organization_name = serializers.StringRelatedField(source = 'organization.name')
    procedure = ProcedureSerializer(many=True)
    class Meta:
        model=Practice
        fields = ['id','name','location','organization','organization_name','procedure']


