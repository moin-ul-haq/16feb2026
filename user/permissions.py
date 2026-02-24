from rest_framework.permissions import BasePermission

class CreateUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'superadmin'


class CreatePatientPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['superadmin','orgadmin','pracadmin']


    