from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from api.views import ItemsListView, OrderCreateView, OrderListView

urlpatterns = [
    path("menu", ItemsListView.as_view(), name="menu"),
    path("order", OrderCreateView.as_view(), name="order"),
    path("orders", OrderListView.as_view(), name="orders"),
    path("docs/", SpectacularAPIView.as_view(), name="docs"),
    # Optional UI:
    path(
        "docs/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="docs"),
        name="swagger-ui",
    ),
    path(
        "docs/redoc/",
        SpectacularRedocView.as_view(url_name="docs"),
        name="redoc",
    ),
]
