from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ServiceArea
from service_area.serializers import PolygonsSerializer, ServiceAreaSerializer

# Create your views here.

class ServiceAreaAPIView(viewsets.ViewSet):
    """
    CRUD operations for service area
    """
   
    def list(self, request):
        serializer = ServiceAreaSerializer(ServiceArea.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })


    def create(self, request):
        serializer = ServiceAreaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data
        }, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        role = ServiceArea.objects.get(id=pk)
        serializer = ServiceAreaSerializer(role)

        return Response({
            'data':serializer.data
        })


    def update(self, request, pk=None):
        role = ServiceArea.objects.get(id=pk)
        serializer = ServiceAreaSerializer(instance=role, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data
        }, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        role = ServiceArea.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PolygonsAPIView(viewsets.ViewSet):
    """
    returns list of service areas where given lat and long matches
    """
    def list(self, request, lat, long):
        serializer = PolygonsSerializer(ServiceArea.objects.filter(
                                                                lat=float(lat), 
                                                                long=float(long)), 
                                                                many=True)
        return Response({
            'data': serializer.data
        })