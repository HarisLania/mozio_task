from rest_framework import serializers
from .models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderRelatedField(serializers.RelatedField):
    """
    Helps in displaying foreign key data
    """
    def to_representation(self, instance):
        return ProviderSerializer(instance).data
    
    def to_internal_value(self, data):
        return self.queryset.get(pk=data)