from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .admin_views import (
    AdminCategoryViewSet,
    AdminSubcategoryViewSet,
    AdminProductViewSet,
    AdminProductAttributeViewSet,
    AdminAttributeValueViewSet,
    AdminPrintSpecsViewSet,
    AdminProductImageViewSet,
    AdminProductReviewViewSet,
)

router = DefaultRouter()
router.register('categories', AdminCategoryViewSet, basename='admin-categories')
router.register('subcategories', AdminSubcategoryViewSet, basename='admin-subcategories')
router.register('products', AdminProductViewSet, basename='admin-products')
router.register('attributes', AdminProductAttributeViewSet, basename='admin-attributes')
router.register('attribute-values', AdminAttributeValueViewSet, basename='admin-attribute-values')
router.register('print-specs', AdminPrintSpecsViewSet, basename='admin-print-specs')
router.register('product-images', AdminProductImageViewSet, basename='admin-product-images')
router.register('product-reviews', AdminProductReviewViewSet, basename='admin-product-reviews')

urlpatterns = [
    path('', include(router.urls)),
]
