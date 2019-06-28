
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from payments.serializers import PaymentSerializer


class PaymentCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(contract_id = self.kwargs['contract_id'])

