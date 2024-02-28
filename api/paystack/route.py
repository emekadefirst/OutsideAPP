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
            payment = Payment.objects.create(user=user, email=email, amount=amount, status=Payment.TRANSACTION_STATUS.PENDING)
            payment.save()
            
            paystack = Paystack(email, amount, secret_key)
            response = paystack.initialize_transaction()
            if response.get("status"):
                auth_url = response["data"]["authorization_url"]
                ref_id = response["data"]["reference"]
                status = paystack.payment_status()  # Assuming this returns 'success' or 'failed'
                if status == 'success':
                    payment.status = Payment.TRANSACTION_STATUS.SUCCESSFUL
                    payment.save()
                else:
                    payment.status = Payment.TRANSACTION_STATUS.FAILED
                    payment.save()
                return Response({"authorization_url": auth_url, "reference": ref_id},  status=200)
            else:
                payment.status = Payment.TRANSACTION_STATUS.FAILED
                payment.save()
                return Response({"message": "Failed to initialize transaction"},  status=400)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





