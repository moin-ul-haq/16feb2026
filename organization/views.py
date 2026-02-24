from .models import *
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from .serializers import *
from .permissions import IsOrgOwnerOrReadOnly,IsPraOwnerOrReadOnly,IsSuperAdmin,IsOrgAdmin,IsPracAdmin
from rest_framework.viewsets import ViewSet,ModelViewSet



# class OrganizationViewSet(ViewSet,ModelViewSet):
#     serializer_class=OrganizationSerializer
#     authentication_classes=User
#     def get_queryset(self):
#         return super().get_queryset()
    
    



# class UserCreateView(mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=User.objects.all()
#     serializer_class = UserSerializer

#     def post(self,request):
#         return self.create(request)
    

# class UserAuthView(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=User.objects.get




# class OrganizationView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Organization.objects.all()
#     serializer_class=OrganizationSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    

class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsOrgAdmin]
    ordering_fields = ['created_at','name']
    search_fields = ['name']
    

    def get_queryset(self):
        user = self.request.user
        if user.role == 'superadmin':
            return Organization.objects.all()
        return Organization.objects.filter(pk = user.organization.pk)
    




# class ProcedureView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Procedure.objects.all()
#     serializer_class=ProcedureSerializer

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)

class ProcedureViewSet(ModelViewSet):
    queryset = Procedure.objects.all()    
    serializer_class = ProcedureSerializer
    permission_classes = [IsPraOwnerOrReadOnly]
    authentication_classes =[TokenAuthentication,SessionAuthentication]
    filterset_fields = ['cost','practice']
    search_fields = ['name','practice__name']
    ordering_fields = ['created_at','name','cost']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'superadmin':
            return Procedure.objects.all()
        return Procedure.objects.filter(practice__organization = user.practice.organization)
    
# class PracticeView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Practice.objects.all()
#     serializer_class=PracticeSerializer

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
class PracticeViewSet(ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [IsPraOwnerOrReadOnly]
    filterset_fields = ['organization','location']
    search_fields = ['name','location','organization__name']
    ordering_fields = ['created_at','name','location']
    authentication_classes=[SessionAuthentication,TokenAuthentication]


    def get_queryset(self):
        user = self.request.user
        if user.role == 'superadmin':
            return Practice.objects.all()
        return Practice.objects.filter(organization = user.organization)

    
# class OrganizationDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Organization.objects.all()
#     serializer_class=OrganizationSerializer


#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# class PracticeDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Practice.objects.all()
#     serializer_class=PracticeSerializer


#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# class ProcedurDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Procedure.objects.all()
#     serializer_class=ProcedureSerializer


#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
