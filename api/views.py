from rest_framework import generics

from api.serializers import ItemSerializer
from pos.models import Item


class ItemsListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.select_related("category").all()
