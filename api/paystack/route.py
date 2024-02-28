from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers.purchase import PurchaseSerializer
from api.models.transaction import Payment
from api.paystack.main import Paystack, secret_key 
from django.http import Http404
from django.utils import timezone

class Checkout(APIView):
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            amount = serializer.validated_data.get('amount')
            user_id = request.user.id
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise Http404("User does not exist")
            
            payment = Payment.objects.create(user_id=user_id, email=email, amount=amount)
            payment.save()
        else:
            return Response({"message": "Wrong input"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Initialize Paystack instance
        paystack = Paystack(email=email, amount=amount, secret_key=secret_key)
        
        # Initialize payment transaction
        response = paystack.initialize_transaction()
        ref_id = response["data"]["reference"]
        
        # Get payment status
        verify = paystack.payment_status()
        
        # Process payment status
        if verify and verify.get("status") == 'success':  # Check if verify is not None
            payment.status = Payment.TRANSACTION_STATUS.SUCCESSFUL
            payment.save()
            return Response({"message": "Your payment has been initiated successfully"}, status=status.HTTP_201_CREATED)
        else:
            payment.status = Payment.TRANSACTION_STATUS.PENDING
            payment.save()
            return Response({"response": response, "message": "Your payment was not initiated successfully"}, status=status.HTTP_400_BAD_REQUEST)
