from rest_framework import viewsets, permissions, filters
from .models import Category, Subcategory, Product
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Categories (Top Level).
    """
    queryset = Category.objects.filter(is_active=True).order_by('display_order')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubcategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Subcategories.
    """
    queryset = Subcategory.objects.filter(is_active=True).order_by('display_order')
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        # If accessed via nested route, filter by category
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            queryset = queryset.filter(category_id=category_pk)
        return queryset

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Products.
    """
    queryset = Product.objects.filter(is_active=True).prefetch_related('attributes__values', 'print_specs')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'sku', 'description']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # If accessed via nested route /subcategories/{id}/products/
        subcategory_pk = self.kwargs.get('subcategory_pk')
        if subcategory_pk:
            queryset = queryset.filter(subcategory_id=subcategory_pk)
            return queryset
        
        # Filter by Subcategory Slug (query param)
        subcategory_slug = self.request.query_params.get('subcategory', None)
        if subcategory_slug:
            queryset = queryset.filter(subcategory__slug=subcategory_slug)
            
        # Filter by Parent Category Slug (query param)
        category_slug = self.request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(subcategory__category__slug=category_slug)
            
        return queryset
