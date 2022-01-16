from decimal import Decimal

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from pos.models import Item, Order, Payment

EMPTY_ITEMS_ERROR_MESSAGE = "Items cannot be empty"
ZERO_TOTAL_ERROR_MESSAGE = "Total cannot be zero"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "category", "image_id", "name", "price"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all()
    )
    payment = PaymentSerializer()

    class Meta:
        model = Order
        fields = ["total", "items", "payment"]

    def create(self, validated_data):
        items = validated_data.pop("items")
        if not items:
            raise ParseError(EMPTY_ITEMS_ERROR_MESSAGE)
        total = Decimal(validated_data.get("total", "0"))
        if total.is_zero():
            raise ParseError(ZERO_TOTAL_ERROR_MESSAGE)
        payment = Payment.objects.create(**validated_data.pop("payment"))
        order = Order.objects.create(total=total, payment=payment)
        order.items.add(*items)
        return order
