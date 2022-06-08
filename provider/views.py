from functools import partial
from provider.models import Provider
from provider.serializers import ProviderSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class ProviderAPIView(viewsets.ViewSet):
    """
    CRUD operations for provider
    """
   
    def list(self, request):
        serializer = ProviderSerializer(Provider.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })


    def create(self, request):
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data
        }, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        role = Provider.objects.get(id=pk)
        serializer = ProviderSerializer(role)

        return Response({
            'data':serializer.data
        })


    def update(self, request, pk=None):
        role = Provider.objects.get(id=pk)
        serializer = ProviderSerializer(instance=role, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data
        }, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        role = Provider.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)