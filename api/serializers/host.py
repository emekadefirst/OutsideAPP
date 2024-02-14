from rest_framework import serializers
from models.host import Host, BankDetail

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        field = '__all__'
        
class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        field = ['bank', 'acc_number', 'acc_name', 'email']
        
        def create(self, validated_data):
            host = Host.objects.create(
                bank=validated_data['bank'],
                acc_number=validated_data['acc_number'],
                acc_name=validated_data['acc_name'],
                first_name=validated_data['first_name'],
                middle_name=validated_data['middle_name'],
                last_name=validated_data['last_name'],
                phone_number=validated_data['phone_number'],
                address=validated_data['address'],
            )
            return host