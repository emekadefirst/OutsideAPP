from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.host import Host
from api.serializers.event import TicketTypeSerializer
from api.serializers.host import HostSerializer, BankDetailSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


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
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Create Create Ticket-Type"""
class CreateTicketType(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        user = request.user  
        try:
            host = Host.objects.get(user=user)  # Retrieve the host associated with the user
        except Host.DoesNotExist:
            return Response({"error": "Only hosts can create ticket types"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = TicketTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['host'] = host
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

"""Host Bank Detail"""
class HostAccountDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        user = request.user  
        try:
            host = Host.objects.get(user=user)  # Retrieve the host associated with the user
        except Host.DoesNotExist:
            return Response({"error": "Only hosts can create account details"}, status=status.HTTP_403_FORBIDDEN)

        serializer = BankDetailSerializer(data=request.data)
        if serializer.is_valid():
            # If the user is a host, associate the bank detail with the host and save
            serializer.validated_data['host'] = host
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

{
    "email": "adams@mail.com",
    "username": "adam12",
    "password": "asddffg"
}

{
    "email": "adams@mail.com",
    "password": "asddffg"
}