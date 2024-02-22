from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.user import UserSerializer, UserLoginSerializer
from django.db.models import Q
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            if created:
                return Response({'message': 'User created successfully', 'token': token.key}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'User already exists', 'token': token.key}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""Login"""
class LoginUser(APIView):
    serializer = UserLoginSerializer
    def post(self, request):
            email = request.data.get('email')
            password = request.data.get('password')
            
            if email is None or password is None:
                return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(email=email).first()

            if user is None or not user.check_password(password):
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer()
            return Response({'message': 'Login successful', 'success': True, 'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        
"""Buy Ticket"""
class BuyTicket(APIView):
    pass