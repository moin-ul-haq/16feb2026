from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer,User
from organization.permissions import IsSuperAdmin

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsSuperAdmin]
