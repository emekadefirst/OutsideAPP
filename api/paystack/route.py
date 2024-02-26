from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers.purchase import PurchaseSerializer
from api.models.transaction import Payment
from api.paystack.main import Paystack, secret_key  # Import Paystack class from main.py

from django.http import Http404

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
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise Http404("User does not exist")
            
            # Create and save the Payment instance
            payment = Payment.objects.create(user=user, amount=amount)  # Replace ... with other required fields
            payment.save()
            
            # Initialize the transaction using Paystack
            paystack = Paystack(email, amount, secret_key)  # Pass secret_key from main.py
            response = paystack.initialize_transaction()
            
            # Print the response to the terminal
            print("Paystack Response:", response)
            
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
class AuthUrl(APIView):
    def get(self, request):
        # Assuming you have the authorization URL stored somewhere or dynamically generated
        authorization_url = "https://checkout.paystack.com/zar52gfvgmf56f9"
        
        # Create the response data
        data = {
            "status": True,
            "message": "Authorization URL created",
            "data": {
                "authorization_url": authorization_url
            }
        }
        
        return Response(data, status=status.HTTP_200_OK)
