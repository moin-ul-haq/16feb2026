
from .serializers import *
from .models import *
from rest_framework import mixins
from rest_framework import generics



class ClaimsView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

class ClaimsDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Claim.objects.all()
    serializer_class=ClaimSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)





