from rest_framework import generics

from api.serializers import ItemSerializer, OrderSerializer
from pos.models import Item, Order


class ItemsListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.select_related("category").all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
