import random
from http import HTTPStatus

import pytest
from model_bakery import baker

from api.serializers import EMPTY_ITEMS_ERROR_MESSAGE, ZERO_TOTAL_ERROR_MESSAGE
from pos.models import Item, Payment

ITEMS_QUANTITY_FIXTURE = random.randint(1, 10)
MENU_ENDPOINT = "/api/v1/menu"
ORDER_ENDPOINT = "/api/v1/order"


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def items():
    return baker.make(Item, _quantity=ITEMS_QUANTITY_FIXTURE)


@pytest.fixture
def payment_dict():
    payment = baker.prepare(Payment, address="Some address")
    return {
        "payment": {
            "name": payment.name,
            "email": payment.email,
            "address": payment.address,
            "payment_mode": payment.payment_mode,
        }
    }


@pytest.mark.django_db
def test_get_menu_items(items, api_client):
    response = api_client.get(MENU_ENDPOINT)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == ITEMS_QUANTITY_FIXTURE


@pytest.mark.django_db
def test_submit_order(items, payment_dict, api_client):
    payload = {
        "items": [item.id for item in items],
        "total": "91.45",
        **payment_dict,
    }
    response = api_client.post(ORDER_ENDPOINT, payload, format="json")
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_submit_order_empty_items(items, payment_dict, api_client):
    payload = {"items": [], "total": "91.45", **payment_dict}
    response = api_client.post(ORDER_ENDPOINT, payload, format="json")
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert {"detail": EMPTY_ITEMS_ERROR_MESSAGE} == response.json()


@pytest.mark.django_db
def test_submit_order_total_zero(items, payment_dict, api_client):
    payload = {
        "items": [item.id for item in items],
        "total": "0.00",
        **payment_dict,
    }
    response = api_client.post(ORDER_ENDPOINT, payload, format="json")
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert {"detail": ZERO_TOTAL_ERROR_MESSAGE} == response.json()
