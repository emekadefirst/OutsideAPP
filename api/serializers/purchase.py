from rest_framework import serializers
from django.contrib.auth.models import User
from api.models.transaction import Payment

class PurchaseSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Payment
        fields = ['email', 'amount', 'quantity']
