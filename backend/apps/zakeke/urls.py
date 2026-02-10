from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZakekeViewSet

router = DefaultRouter()
router.register(r'', ZakekeViewSet, basename='zakeke')

urlpatterns = [
    # Alias for when Zakeke appends IDs to the catalog endpoint base URL
    # Logs show Zakeke requesting: /api/v1/zakeke/catalog/<ID>/options
    path('catalog/<str:pk>/options', ZakekeViewSet.as_view({'get': 'product_options'}), name='zakeke-options-catalog-alias'),

    # Explicitly handle no-slash for Zakeke options endpoint
    # Zakeke often requests this without a trailing slash, and Django/DRF defaults to requiring one.
    path('<str:pk>/options', ZakekeViewSet.as_view({'get': 'product_options'}), name='zakeke-options-noslash'),
    
    path('', include(router.urls)),
]
