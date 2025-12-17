from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .admin_views import AdminCategoryViewSet, AdminSubcategoryViewSet, AdminProductViewSet

router = DefaultRouter()
router.register(r'categories', AdminCategoryViewSet, basename='admin-category')
router.register(r'subcategories', AdminSubcategoryViewSet, basename='admin-subcategory')
router.register(r'products', AdminProductViewSet, basename='admin-product')

urlpatterns = [
    path('', include(router.urls)),
]
