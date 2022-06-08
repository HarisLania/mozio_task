from provider.models import Provider
from provider.serializers import ProviderSerializer
from rest_framework import generics, mixins
from rest_framework.response import Response
# Create your views here.


class ProviderGenericAPIView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin, 
                            mixins.DestroyModelMixin):
    """
    CRUD operations for provider
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

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
