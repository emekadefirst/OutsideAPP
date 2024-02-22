from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.event import EventSerializer
from django.db.models import Q
from rest_framework import status
from django.db.models.functions import Lower
from rest_framework.pagination import PageNumberPagination
from api.models.event import Event


"""Provide list of event 25 per request"""
class EventView(APIView):
    pagination_class = PageNumberPagination

    # def get_queryset(self):
    #     return Event.objects.all()

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
# class SearchEventView(APIView):
#     permission_classes = []  # Remove all permission classes

#     def post(self, request):
#         search_query = request.data.get('query', '')
#         if search_query:
#             search_results = Event.objects.filter(
#                 Q(name__icontains=search_query) |
#                 Q(date__icontains=search_query) |
#                 Q(venue__icontains=search_query) |
#                 Q(banner__icontains=search_query) |
#                 Q(host__icontains=search_query)
#             ).order_by(Lower('name'))

#             serializer = EventSerializer(search_results, many=True)
#             return Response(serializer.data)
#         else:
#             return Response("Invalid search query", status=status.HTTP_400_BAD_REQUEST)
        
        
"""Create Event"""
class CreateEvent(APIView):
    def post(self, request):
        serializer = EventSerializer
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
