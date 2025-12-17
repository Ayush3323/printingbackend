from rest_framework import serializers
from .models import SavedDesign, Asset, Template, Font

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'user', 'file', 'type', 'original_filename', 'size_bytes', 'mime_type', 'resolution_dpi', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class SavedDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedDesign
        fields = ['id', 'user', 'product', 'name', 'design_json', 'preview_image', 'version', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class TemplateSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.ReadOnlyField(source='subcategory.name')
    class Meta:
        model = Template
        fields = ['id', 'product', 'name', 'description', 'design_json', 'subcategory', 'subcategory_name', 'tags', 'preview_image']

class FontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Font
        fields = ['id', 'name', 'family', 'file', 'weight', 'style']
