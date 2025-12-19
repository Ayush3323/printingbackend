from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Subcategory, Product, ProductAttribute, AttributeValue, PrintSpecs, ProductImage, ProductReview
from .serializers import (
    CategorySerializer, SubcategorySerializer, ProductSerializer,
    ProductAttributeSerializer, AttributeValueSerializer, PrintSpecsSerializer,
    ProductImageSerializer, ProductReviewSerializer
)
from apps.users.permissions import IsAdminOrStaff

class AdminCategoryViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing categories.
    """
    queryset = Category.objects.all().order_by('display_order')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get category statistics"""
        total = Category.objects.count()
        active = Category.objects.filter(is_active=True).count()
        return Response({
            'total': total,
            'active': active,
            'inactive': total - active,
        })

class AdminSubcategoryViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing subcategories.
    """
    queryset = Subcategory.objects.all().select_related('category').order_by('display_order')
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug', 'category__name']

class AdminProductViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing products.
    """
    queryset = Product.objects.all().select_related('subcategory__category').prefetch_related('attributes__values', 'print_specs')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'sku', 'description', 'subcategory__name']
    ordering_fields = ['created_at', 'base_price', 'stock_quantity']
    ordering = ['-created_at']

    @action(detail=False, methods=['post'])
    def bulk_update_stock(self, request):
        """Bulk update stock quantities"""
        updates = request.data.get('updates', [])
        for update in updates:
            product_id = update.get('id')
            stock = update.get('stock_quantity')
            if product_id and stock is not None:
                Product.objects.filter(id=product_id).update(stock_quantity=stock)
        return Response({'status': 'Stock updated'})

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get product statistics"""
        total = Product.objects.count()
        active = Product.objects.filter(is_active=True).count()
        low_stock = Product.objects.filter(stock_quantity__lt=10, is_infinite_stock=False).count()
        
        return Response({
            'total': total,
            'active': active,
            'inactive': total - active,
            'low_stock': low_stock,
        })

class AdminProductAttributeViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing product attributes.
    """
    queryset = ProductAttribute.objects.all().select_related('product').prefetch_related('values')
    serializer_class = ProductAttributeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'product__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product', None)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset

    def create(self, request, *args, **kwargs):
        """Create attribute with values"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract nested values
        values_data = request.data.get('values', [])
        attribute = ProductAttribute.objects.create(
            product_id=request.data['product'],
            name=request.data['name'],
            display_name=request.data.get('display_name', ''),
            attribute_type=request.data.get('attribute_type', 'text'),
            is_required=request.data.get('is_required', True),
            display_order=request.data.get('display_order', 0)
        )
        
        # Create values
        for val_data in values_data:
            AttributeValue.objects.create(
                attribute=attribute,
                value=val_data['value'],
                display_value=val_data.get('display_value', ''),
                price_adjustment=val_data.get('price_adjustment', 0),
                is_default=val_data.get('is_default', False),
                swatch_color=val_data.get('swatch_color', ''),
            )
        
        return Response(ProductAttributeSerializer(attribute).data, status=status.HTTP_201_CREATED)

class AdminAttributeValueViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing attribute values.
    """
    queryset = AttributeValue.objects.all().select_related('attribute__product')
    serializer_class = AttributeValueSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]

    def get_queryset(self):
        queryset = super().get_queryset()
        attribute_id = self.request.query_params.get('attribute', None)
        if attribute_id:
            queryset = queryset.filter(attribute_id=attribute_id)
        return queryset

class AdminPrintSpecsViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing print specifications.
    """
    queryset = PrintSpecs.objects.all().select_related('product')
    serializer_class = PrintSpecsSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product', None)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset

class AdminProductImageViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing product images.
    """
    queryset = ProductImage.objects.all().select_related('product')
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product', None)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset

class AdminProductReviewViewSet(viewsets.ModelViewSet):
    """
    Admin-only ViewSet for managing product reviews.
    """
    queryset = ProductReview.objects.all().select_related('product', 'user')
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrStaff]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'comment', 'user__email', 'product__name']
    ordering_fields = ['rating', 'created_at', 'helpful_count']
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product', None)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset
    
    @action(detail=True, methods=['post'])
    def mark_helpful(self, request, pk=None):
        """Increment helpful count"""
        review = self.get_object()
        review.helpful_count += 1
        review.save()
        return Response({'helpful_count': review.helpful_count})

