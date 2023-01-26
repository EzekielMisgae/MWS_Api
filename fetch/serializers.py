from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'amazon_order_id', 'purchase_date', 'last_update_date', 'order_status', 'fulfillment_channel', 'sales_channel', 'order_total', 'number_of_items_shipped', 'number_of_items_unshipped', 'payment_execution_detail', 'payment_method')
