from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from .models import ServiceArea
from service_area.serializers import PolygonsSerializer, ServiceAreaSerializer

# Create your views here.

class ServiceAreaGenericAPIView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin, 
                            mixins.DestroyModelMixin):
    """
    CRUD operations for service area
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })
        return Response({
                'data': self.list(request).data
            })


    def post(self, request):
        return Response({
            'data': self.create(request).data
        })
    
    def put(self, request, pk=None):
        if pk:
            return Response({
                'data': self.update(request, pk).data
            })
    
    def patch(self, request, pk=None):
        if pk:
            return Response({
                'data': self.partial_update(request, pk).data
            })

    def delete(self, request, pk=None):
        if pk:
            return self.destroy(request, pk)



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