from django.urls import path,include
from organization.urls import router


urlpatterns = [
    path('',include(router.urls))
]
