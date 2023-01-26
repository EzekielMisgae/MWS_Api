from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer
from .tasks import fetch_order_history

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def fetch_orders(self, request):
        """
        Fetches the order history for the authenticated user
        and creates Order objects in the database.
        """
        user = request.user
        fetch_order_history.delay(user.pk)
        return Response({'status': 'Order history is being fetched'})

    @action(detail=True, methods=['get'])
    def retrieve_order(self, request, pk=None):
        """
        Retrieves a specific order for the authenticated user.
        """
        user = request.user
        order = get_object_or_404(Order, user=user, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)