import os
import json
import requests
from dotenv import load_dotenv
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers.purchase import PurchaseSerializer
from api.models.transaction import Payment

class Checkout(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            amount = serializer.validated_data.get('amount')
            
            # Retrieve the User object from the database
            user_id = request.user.id  # Example: You might get the user ID from the request
            user = User.objects.get(id=user_id)
            
            # Create and save the Payment instance
            payment = Payment.objects.create(user=user, amount=amount)  # Replace ... with other required fields
            payment.save()
            
            # Initialize the transaction using Paystack
            paystack = Paystack(email, amount, sk)
            response = paystack.initialize_transaction()
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Paystack:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount
        self.secret_key = secret_key

    def initialize_transaction(self):
        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": "Bearer " + self.secret_key,
            "Content-Type": "application/json"
        }
        data = {
            "email": self.email,
            "amount": self.amount
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()


load_dotenv()
sk = os.environ.get("PAYSTACK_PIR_KEY")

