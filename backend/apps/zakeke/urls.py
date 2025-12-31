from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZakekeViewSet

router = DefaultRouter()
router.register(r'', ZakekeViewSet, basename='zakeke')

urlpatterns = [
    path('', include(router.urls)),
]
