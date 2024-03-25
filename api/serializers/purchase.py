from rest_framework import serializers
from api.models.transaction import Payment, PaymentDetail

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'email', 'amount', 'status', 'reference', 'time']
        read_only_fields = ['status', 'reference', 'time'] 
class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = ['id', 'user', 'quantity', 'ticket', 'payment', 'time']
        read_only_fields = ['payment', 'time']  

    def validate(self, data):
        """
        Validate the data before saving it.
        """
        # Example validation: Ensure quantity is not negative
        quantity = data.get('quantity', 0)
        if quantity < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        
        return data
