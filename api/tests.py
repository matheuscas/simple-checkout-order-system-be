import random

import pytest
from model_bakery import baker

from pos.models import Item

ITEMS_QUANTITY_FIXTURE = random.randint(1, 10)
MENU_ENDPOINT = "/api/v1/menu"


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def items():
    baker.make(Item, _quantity=ITEMS_QUANTITY_FIXTURE)


@pytest.mark.django_db
def test_get_menu_items(items, api_client):
    response = api_client.get(MENU_ENDPOINT)
    assert response.status_code == 200
    assert len(response.json()) == ITEMS_QUANTITY_FIXTURE
