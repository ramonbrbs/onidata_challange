from rest_framework import mixins
from rest_framework import generics
from contracts.serializers import ContractSerializer
from rest_framework.permissions import IsAuthenticated
from contracts.models import Contract
from contracts import util

class ContractListView(generics.ListCreateAPIView):
    """
       get:
       Returns a list of contracts

       post:
       Creates a new contract for registered user
       """
    permission_classes = (IsAuthenticated,)
    serializer_class = ContractSerializer

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, ip_address = util.get_client_ip(self.request))


class ConctractDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContractSerializer

    def get_queryset(self):
        user = self.request.user
        print(self.kwargs['pk'])
        return Contract.objects.filter(user=user)