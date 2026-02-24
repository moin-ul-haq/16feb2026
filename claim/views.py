from .serializers import *
from .models import *
from rest_framework import viewsets
from organization.permissions import IsPraOwnerOrReadOnly



class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsPraOwnerOrReadOnly]
    filterset_fields = ['practice','status','patient']
    search_fields = ['practice','status']
    ordering_fields = ['status','created_at','total_amount']

    def get_queryset(self):
        if self.request.user.role == 'superadmin':
            return Claim.objects.all()
        return Claim.objects.filter(practice__organization__id = self.request.user.practice.organization.id)
