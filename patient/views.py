from rest_framework.permissions import IsAdminUser
from user.permissions import CreatePatientPermission
from .serializers import PatientSerializer
from .models import Patient
from rest_framework import viewsets
from organization.permissions import IsPraOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsPraOwnerOrReadOnly]
    filterset_fields = ['organization','practice']
    search_fields = ['name','organization__name','practice__name','email']
    ordering_fields = ['name','created_at','age']
    
    # authentication_classes = []
    def get_queryset(self):
        user = self.request.user
        if user.role == 'superadmin':
            return Patient.objects.all()
        return Patient.objects.filter(organization = user.organization)
    


# # class ClaimsView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
# #     queryset = Claim.objects.all()
# #     serializer_class = ClaimSerializer

# #     def get(self,request):
# #         return self.list(request)
# #     def post(self,request):
# #         return self.create(request)
    

# # class ClaimsDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
# #     queryset=Claim.objects.all()
# #     serializer_class=ClaimSerializer

# #     def get(self,request,pk):
# #         return self.retrieve(request,pk)
# #     def put(self,request,pk):
# #         return self.update(request,pk)
# #     def delete(self,request,pk):
# #         return self.destroy(request,pk)



# class ClaimViewSet(viewsets.ModelViewSet):
#     queryset = Claim.objects.filter(status = 'successfull')
#     serializer_class = ClaimSerializer


