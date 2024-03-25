import os
from django.contrib.auth.models import User
from dotenv import load_dotenv
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api.models.transaction import Payment
from api.serializers.purchase import PaymentSerializer, PaymentDetailSerializer
from .payment import Pay
from .status import Verify

load_dotenv()
PAYSTACK_SECRET_KEY = os.environ.get("PAYSTACK_SECRET_KEY")

class Checkout(APIView):
    def post(self, request):
        payment_detail_serializer = PaymentDetailSerializer(data=request.data)
        if payment_detail_serializer.is_valid():
            email = payment_detail_serializer.validated_data.get('email')
            amount = payment_detail_serializer.validated_data.get('amount')
            user_id = request.user.id

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            # Creating Payment instance using serializer data
            payment_data = {
                'user': user_id,
                'email': email,
                'amount': amount,
            }
            payment_serializer = PaymentSerializer(data=payment_data)
            if payment_serializer.is_valid():
                payment = payment_serializer.save()
            else:
                return Response({"message": "Invalid payment data"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create PaymentDetail instance and associate it with Payment
            payment_detail_data = {
                'user': user_id,
                'quantity': payment_detail_serializer.validated_data.get('quantity'),
                'ticket': payment_detail_serializer.validated_data.get('ticket'),
                'payment': payment.id,  # Associate Payment with PaymentDetail
            }
            payment_detail_serializer = PaymentDetailSerializer(data=payment_detail_data)
            if payment_detail_serializer.is_valid():
                payment_detail_serializer.save()
            else:
                return Response({"message": "Invalid payment detail data"}, status=status.HTTP_400_BAD_REQUEST)

            # Initiating payment transaction
            paid = Pay(email, amount, PAYSTACK_SECRET_KEY)
            response = paid.initialize_transaction()
            if response:
                ref_id = response.get("data", {}).get("reference")
                auth_url = response.get("data", {}).get("authorization_url")
                if ref_id and auth_url:
                    return Response({
                        "message": "Payment initialized successfully",
                        "reference": ref_id,
                        "authorization_url": auth_url
                    }, status=status.HTTP_201_CREATED)
            return Response({"message": "Failed to initialize payment"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(payment_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            
    def status(self, request):
        ref_id = request.data.get('reference')
        if ref_id:
            try:
                payment = Payment.objects.get(reference=ref_id)
            except Payment.DoesNotExist:
                return Response({"message": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

            verify = Verify(ref_id, PAYSTACK_SECRET_KEY)
            status_result = verify.status()

            if status_result == 'successful':
                payment.status = Payment.TRANSACTION_STATUS.SUCCESSFUL
                return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)
            elif status_result == 'pending':
                payment.status = Payment.TRANSACTION_STATUS.PENDING
                return Response({"message": "Payment failed or pending"}, status=status.HTTP_102_PROCESSING)
            else:
                payment.status = Payment.TRANSACTION_STATUS.FAILED
                return Response({"message": "Payment failed or pending"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Reference ID not provided"}, status=status.HTTP_400_BAD_REQUEST)            