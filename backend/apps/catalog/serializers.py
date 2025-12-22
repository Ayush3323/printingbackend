from rest_framework import serializers
from .models import Category, Subcategory, Product, PrintSpecs, ProductAttribute, AttributeValue, ProductImage, ProductReview, Banner



class ProductMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'primary_image', 'is_featured']

class SubcategorySerializer(serializers.ModelSerializer):
    products = ProductMinimalSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'description', 'image', 'category', 'products']

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

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'alt_text', 'display_order', 'is_primary', 'created_at']
        read_only_fields = ['created_at']

class ProductReviewSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductReview
        fields = ['id', 'product', 'user', 'user_email', 'user_name', 'rating', 'title', 'comment', 
                  'is_verified_purchase', 'helpful_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'helpful_count']
    
    def get_user_name(self, obj):
        return obj.user.get_full_name() if hasattr(obj.user, 'get_full_name') else obj.user.email


class ProductSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.ReadOnlyField(source='subcategory.name')
    attributes = ProductAttributeSerializer(many=True, required=False)
    print_specs = PrintSpecsSerializer(required=False)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)
    final_price = serializers.ReadOnlyField()
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'subcategory', 'subcategory_name', 'name', 'slug', 'sku',
            'description', 'base_price', 'stock_quantity', 
            'discount_type', 'discount_value', 'discount_start_date', 'discount_end_date', 'is_on_sale',
            'final_price', 'primary_image', 'images',
            'attributes', 'print_specs', 'reviews', 'average_rating', 'review_count',
            'meta_title', 'meta_description', 'is_active', 'is_featured'
        ]
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(r.rating for r in reviews) / len(reviews)
        return 0
    
    def get_review_count(self, obj):
        return obj.reviews.count()

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
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.base_price = validated_data.get('base_price', instance.base_price)
        instance.discount_type = validated_data.get('discount_type', instance.discount_type)
        instance.discount_value = validated_data.get('discount_value', instance.discount_value)
        instance.is_on_sale = validated_data.get('is_on_sale', instance.is_on_sale)
        instance.primary_image = validated_data.get('primary_image', instance.primary_image)
        instance.save()
        return instance

class BannerSerializer(serializers.ModelSerializer):
    buttons = serializers.SerializerMethodField()
    footer = serializers.CharField(source='footer_text', read_only=True)
    
    class Meta:
        model = Banner
        fields = ['id', 'title', 'subtitle', 'image', 'placement', 'buttons', 'footer', 
                  'is_active', 'display_order', 'start_date', 'end_date']
    
    def get_buttons(self, obj):
        """Transform buttons_json to match frontend format"""
        return obj.buttons_json if obj.buttons_json else []

