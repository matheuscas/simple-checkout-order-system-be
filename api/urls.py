from django.urls import path

from api.views import ItemsListView, OrderCreateView

urlpatterns = [
    path("menu", ItemsListView.as_view(), name="menu"),
    path("order", OrderCreateView.as_view(), name="order"),
]
