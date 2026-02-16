from django.urls import path
from .views import *


urlpatterns = [
    path('payments/',Paymentview.as_view(),name='payments'),
    path('payments/<int:pk>',PaymentDetailView.as_view(),name='payments_detail'),

]