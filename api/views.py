from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.event import Event, Ticket, TicketType
from .models.host import BankDetail, Host
from .serializers.event import EventSerializer, TicketTypeSerializer
from .serializers.user import UserSerializer, UserLoginSerializer
from .serializers.host import HostSerializer, BankDetailSerializer
from django.db.models import Q
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token

"""Provide list of event 25 per request"""
class EventView(APIView):
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Event.objects.all()

    def get(self, request):
        events = self.get_queryset()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(events, request)

        if page is not None:
            serializer = EventSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""Search through the entire db table i.e host event ticket"""
class SearchEventView(APIView):
    permission_classes = []  # Remove all permission classes

    def post(self, request):
        search_query = request.data.get('query', '')
        if search_query:
            search_results = Event.objects.filter(
                Q(name__icontains=search_query) |
                Q(date__icontains=search_query) |
                Q(venue__icontains=search_query) |
                Q(banner__icontains=search_query) |
                Q(host__icontains=search_query)
            ).order_by(Lower('name'))

            serializer = EventSerializer(search_results, many=True)
            return Response(serializer.data)
        else:
            return Response("Invalid search query", status=status.HTTP_400_BAD_REQUEST)
        
        

"""Create user and generate token for each new user"""

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
        
"""Create Host"""
class HostView(APIView):
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Host.objects.all()

    def get(self, request):
        hosts = self.get_queryset()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(hosts, request)

        if page is not None:
            serializer = HostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = HostSerializer(hosts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Create Event"""
class CreateEvent(APIView):
    def post(self, request):
        serializer = EventSerializer
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Create Create Ticket-Type"""
class CreateTicketType(APIView):
    def post(self, request):
        serializer = TicketTypeSerializer
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""Create Host Account Detail"""
class HostAccountDetail(APIView):
    def post(self, request):
        serializer = BankDetailSerializer
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Buy Ticket"""
class BuyTicket(APIView):
    pass
