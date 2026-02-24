from rest_framework import permissions
from .models import Practice
from payment.models import Payment
from patient.models import Patient
from organization.models import Procedure
from claim.models import Claim

class IsOrgOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'superadmin'
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and ((obj.user == request.user) or request.user.role == 'superadmin')



class IsPraOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['superadmin','orgadmin','pracadmin']
        # return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in ['GET']:
                return True
#Logic For Practice Object
            if isinstance(obj,Practice):
                return request.user.practice.id == obj.pk
#logic for Patient Object
            if isinstance(obj,Patient):
                return request.user.practice.id == obj.practice.id
#logic for Payment Object
            if isinstance(obj,Payment):
                return request.user.practice.id == obj.claim.practice.id
#Logic For Procedure Object and Claim
            if isinstance(obj,Procedure) or isinstance(obj,Claim):
                return request.user.practice.id == obj.practice.id

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'superadmin'
        


class IsOrgAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.role in ['superadmin','orgadmin']



class IsPracAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            # print('----------------')
            return request.user.role in ['superadmin','orgadmin','pracadmin']