from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.event import Event, Ticket, TicketType
from .models.host import BankDetail, Host
from .serializers.event import EventSerializer
from django.db.models import Q
from rest_framework import status
from django.http import HttpResponse
from django.db.models.functions import Lower
from rest_framework.pagination import PageNumberPagination

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

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class SearchEventView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Add this line

    def get_queryset(self):  # Define a queryset method
        return Event.objects.all()

    def post(self, request):
        search_query = request.data.get('query', '')
        print(f"Received search query: {search_query}")

        if search_query is not None:
            search_results = Event.objects.filter(
                Q(name__icontains=search_query) |
                Q(date__icontains=search_query) |
                Q(venue__icontains=search_query) |
                Q(banner__icontains=search_query) |
                Q(host__icontains=search_query)  
            )

            search_results = search_results.order_by(Lower('name'))

            serializer = EventSerializer(search_results, many=True)
            return Response(serializer.data)
        else:
            return Response("Invalid search query", status=status.HTTP_400_BAD_REQUEST)
