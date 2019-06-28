from rest_framework.serializers import ModelSerializer
from contracts.models import Contract
from payments.serializers import PaymentSerializer


class ContractSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Contract
        fields = ('id','amount','amount_due','bank', 'interest_rate', 'submission_date', 'customer_metadata', 'payments')
        #exclude = ('user','ip_address')

