from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
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
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
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


