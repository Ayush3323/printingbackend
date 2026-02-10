from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZakekeViewSet

router = DefaultRouter()
router.register(r'', ZakekeViewSet, basename='zakeke')

urlpatterns = [
    # Explicitly handle no-slash for Zakeke options endpoint
    # Zakeke often requests this without a trailing slash, and Django/DRF defaults to requiring one.
    path('<str:pk>/options', ZakekeViewSet.as_view({'get': 'product_options'}), name='zakeke-options-noslash'),
    
    path('', include(router.urls)),
]
