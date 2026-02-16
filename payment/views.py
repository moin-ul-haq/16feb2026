
from rest_framework import mixins,generics
from .serializers import *
from .models import *


class Paymentview(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class PaymentDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
