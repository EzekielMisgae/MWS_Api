from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fetch_orders/', OrderViewSet.as_view({'get': 'fetch_orders'}), name='fetch_orders'),
    path('retrieve_order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve_order'}), name='retrieve_order'),
]