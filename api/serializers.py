from decimal import Decimal

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from pos.models import Item, Order

EMPTY_ITEMS_ERROR_MESSAGE = "Items cannot be empty"
ZERO_TOTAL_ERROR_MESSAGE = "Total cannot be zero"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "category", "image_id", "name", "price", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all()
    )

    class Meta:
        model = Order
        fields = ["total", "items"]

    def create(self, validated_data):
        items = validated_data.pop("items")
        if not items:
            raise ParseError(EMPTY_ITEMS_ERROR_MESSAGE)
        total = Decimal(validated_data.get("total", "0"))
        if total.is_zero():
            raise ParseError(ZERO_TOTAL_ERROR_MESSAGE)
        order = Order.objects.create(**validated_data)
        order.items.add(*items)
        return order
