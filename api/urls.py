from django.urls import path

from api.views import ItemsListView

urlpatterns = [path("menu", ItemsListView.as_view(), name="menu")]
