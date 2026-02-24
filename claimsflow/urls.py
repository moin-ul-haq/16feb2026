
from django.contrib import admin
from django.urls import path,include
from organization.urls import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('organization.urls')),
    path('api/',include('payment.urls')),
    path('api/',include('patient.urls')),
    path('api/',include('claim.urls')),
    path('api/',include('user.urls')),
    path('auth/',include('rest_framework.urls')),

]
