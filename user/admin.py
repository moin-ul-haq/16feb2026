from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','organization_name']
    
    def organization_name(self,obj):
        if obj.organization:
            return obj.organization.name