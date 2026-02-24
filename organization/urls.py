from django.urls import path,include
from .views import *
from payment.views import PaymentViewSet
from claim.views import ClaimViewSet
from rest_framework.routers import DefaultRouter
from patient.views import PatientViewSet
from user.views import UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router= DefaultRouter()
router.register('organization',OrganizationViewSet,basename='organization')
router.register('practice',PracticeViewSet,basename='practice')
router.register('procedure',ProcedureViewSet,basename= 'procedure')
router.register('payment',PaymentViewSet,basename= 'payment')
router.register('claim',ClaimViewSet, basename= 'claim')
router.register('patient',PatientViewSet, basename= 'patient')
router.register('user',UserViewSet, basename= 'user')




urlpatterns = [
    # path('organizations/',OrganizationView.as_view(),name='organizations'),
    # path('organizations/<int:pk>',OrganizationDetailView.as_view(),name='organization_detail'),
    # path('procedures/',ProcedureView.as_view(),name='procedures'),
    # path('procedures/<int:pk>',ProcedurDetailView.as_view(),name='procedure_detail'),
    # path('practices/',PracticeView.as_view(),name='practices'),
    # path('practices/<int:pk>',PracticeDetailView.as_view(),name='practice_detail'),
    # path('users/',UserCreateView.as_view(),name='user'),
    path('',include(router.urls)),
    path('gettoken/',ObtainAuthToken.as_view())
]
