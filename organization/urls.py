from django.urls import path
from .views import *
from rest_framework.routers import Route,DefaultRouter


# router= DefaultRouter()

# router.register(r'organizationsp',OrganizationViewSet,basename='organizationsp')

# # rou


urlpatterns = [
    path('organizations/',OrganizationView.as_view(),name='organizations'),
    path('organizations/<int:pk>',OrganizationDetailView.as_view(),name='organization_detail'),
    path('procedures/',ProcedureView.as_view(),name='procedures'),
    path('procedures/<int:pk>',ProcedurDetailView.as_view(),name='procedure_detail'),
    path('practices/',PracticeView.as_view(),name='practices'),
    path('practices/<int:pk>',PracticeDetailView.as_view(),name='practice_detail'),
    path('users/',UserCreateView.as_view(),name='user'),

]
