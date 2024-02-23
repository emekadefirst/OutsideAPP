from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from rest_framework import status
from django.contrib.auth.models import User
from api.serializers.user import UserSerializer
from api.paystack.main import Paystack
from dotenv import load_dotenv

load_dotenv()
publickey = os.environ.get("PAYSTACK_PUB_KEY")
secretkey = os.environ.get("PAYSTACK_PIR_KEY")

class Checkout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Assuming the email and amount are sent in the request data
            email = serializer.validated_data.get('email')
            amount = serializer.validated_data.get('amount')

            paystack = Paystack(secretkey, publickey)
            response = paystack.initate_payment(email, amount)
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
