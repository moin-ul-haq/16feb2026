from django.urls import path,include
# from .views import *
from organization.urls import router


urlpatterns = [
    # path('claims/',ClaimsView.as_view(),name='claims'),
    # path('claims/<int:pk>',ClaimsDetailView.as_view(),name='claims_detail'),
    path('',include(router.urls))

]