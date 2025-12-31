from rest_framework import serializers
from apps.catalog.models import Product

class ZakekeCatalogProductSerializer(serializers.ModelSerializer):
    """Serializer for Zakeke's Product Catalog API."""
    code = serializers.CharField(source='id')
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['code', 'name', 'thumbnail']

    def get_thumbnail(self, obj):
        return obj.primary_image if obj.primary_image else None
