from django.db.models import Q
from rest_framework import mixins,generics
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from organization.permissions import IsPraOwnerOrReadOnly




# class Paymentview(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Payment.objects.all()
#     serializer_class=PaymentSerializer

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
# class PaymentDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Payment.objects.all()
#     serializer_class=PaymentSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsPraOwnerOrReadOnly]
    filterset_fields = ['status']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'superadmin':
            return Payment.objects.all()
        return Payment.objects.filter(claim__practice__organization = user.organization)
    