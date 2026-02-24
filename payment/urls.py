from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from organization.urls import router



# router.register('payment',PaymentViewSet,basename= 'payment')


urlpatterns = [
    # path('payments/',Paymentview.as_view(),name='payments'),
    # path('payments/<int:pk>',PaymentDetailView.as_view(),name='payments_detail'),
    path('', include(router.urls)),

]