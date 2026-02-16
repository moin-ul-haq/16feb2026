from django.urls import path
from .views import *


urlpatterns = [
    path('claims/',ClaimsView.as_view(),name='claims'),
    path('claims/<int:pk>',ClaimsDetailView.as_view(),name='claims_detail'),

]