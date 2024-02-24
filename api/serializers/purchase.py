from rest_framework import serializers
from api.models.transaction import Payment

class PurchaseSerilizer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ['email', 'amount', 'quantity']