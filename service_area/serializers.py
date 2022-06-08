from rest_framework import serializers
from .models import ServiceArea
from provider.models import Provider
from provider.serializers import ProviderRelatedField

class ServiceAreaSerializer(serializers.ModelSerializer):
    """
    Service area serializer where fetching the provider's
    data also with help of foreign key
    """
    provider = ProviderRelatedField(many=False,
                                    queryset=Provider.objects.all())
    class Meta:
        model = ServiceArea
        fields = '__all__'


class PolygonsSerializer(serializers.ModelSerializer):
    """
    Serializer for polygon viewset with respect to
    given lat and long
    """
    provider_name = serializers.CharField(source='provider.name',
                                        allow_null=True)
    class Meta:
        model = ServiceArea
        fields = ('name', 'provider_name', 'price')