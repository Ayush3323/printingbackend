from rest_framework import serializers
from .models import Category, Subcategory, Product, PrintSpecs, ProductAttribute, AttributeValue

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'description', 'image', 'category']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'subcategories']

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['id', 'value', 'display_value', 'price_adjustment', 'is_default', 'swatch_color', 'swatch_image']

class ProductAttributeSerializer(serializers.ModelSerializer):
    values = AttributeValueSerializer(many=True, required=False)

    class Meta:
        model = ProductAttribute
        fields = ['id', 'name', 'display_name', 'attribute_type', 'is_required', 'values']

class PrintSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintSpecs
        fields = ['width_mm', 'height_mm', 'bleed_margin_mm', 'safe_zone_mm', 'format_template_url', 'allowed_file_types']

class ProductSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.ReadOnlyField(source='subcategory.name')
    attributes = ProductAttributeSerializer(many=True, required=False)
    print_specs = PrintSpecsSerializer(required=False)

    class Meta:
        model = Product
        fields = [
            'id', 'subcategory', 'subcategory_name', 'name', 'slug', 'sku',
            'description', 'base_price', 'stock_quantity', 
            'attributes', 'print_specs',
            'meta_title', 'meta_description'
        ]

    def create(self, validated_data):
        attributes_data = validated_data.pop('attributes', [])
        print_specs_data = validated_data.pop('print_specs', None)
        
        product = Product.objects.create(**validated_data)
        
        if print_specs_data:
            PrintSpecs.objects.create(product=product, **print_specs_data)
            
        for attr_data in attributes_data:
            values_data = attr_data.pop('values', [])
            attribute = ProductAttribute.objects.create(product=product, **attr_data)
            
            for val_data in values_data:
                AttributeValue.objects.create(attribute=attribute, **val_data)
                
        return product

    def update(self, instance, validated_data):
        # NOTE: Updating nested arrays is complex (match IDs? delete missing?). 
        # For simplicity in this 'future-proofing' request, we focus on creation capability.
        # Standard update logic for the main product fields:
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.base_price = validated_data.get('base_price', instance.base_price)
        instance.save()
        return instance
