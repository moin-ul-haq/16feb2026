from .models import *
from rest_framework import mixins,generics
from .serializers import *
from rest_framework.viewsets import ViewSet,ModelViewSet


# class OrganizationViewSet(ViewSet,ModelViewSet):
#     serializer_class=OrganizationSerializer
#     authentication_classes=User
#     def get_queryset(self):
#         return super().get_queryset()
    
    



class UserCreateView(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

    def post(self,request):
        return self.create(request)
    

class UserAuthView(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=User.objects.get




class OrganizationView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Organization.objects.all()
    serializer_class=OrganizationSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    






class ProcedureView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Procedure.objects.all()
    serializer_class=ProcedureSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

class PracticeView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Practice.objects.all()
    serializer_class=PracticeSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class OrganizationDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Organization.objects.all()
    serializer_class=OrganizationSerializer


    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)


class PracticeDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Practice.objects.all()
    serializer_class=PracticeSerializer


    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)


class ProcedurDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Procedure.objects.all()
    serializer_class=ProcedureSerializer


    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
