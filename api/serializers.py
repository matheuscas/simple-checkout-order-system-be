from rest_framework import serializers

from pos.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "category", "image_id", "name", "price", "quantity"]
