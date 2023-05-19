import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_groups(api_client):
    response = api_client.get(reverse("groups-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_group_create_without_user(api_client):
    payload = {
        "title": "'test'",
        "city": "'Kazan'",
        "description": "'test test test'",
        "categories": []
    }
    response = api_client.post(reverse("groups-list"), data=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content


@pytest.mark.django_db
def test_group_detail(api_client, group):
    response = api_client.get(reverse("groups-detail", args=(group.id, )))
    assert response.status_code == status.HTTP_200_OK
    assert group.id == response.json()["id"]


@pytest.mark.django_db
def test_group_partial_update(api_client, group):
    response = api_client.put(reverse("groups-detail", args=(group.id,)), data={"title": "new_title"})
    assert response.status_code == status.HTTP_200_OK, response.content
    group.refresh_from_db()
    assert group.title == "new_title"


@pytest.mark.django_db
def test_group_categories_update(api_client, group, category):
    payload = {
        "categories": [category.id]
    }
    response = api_client.put(reverse("groups-detail", args=(group.id,)), data=payload)
    assert response.status_code == status.HTTP_200_OK, response.content
    group.refresh_from_db()
    assert group.categories.count() == 1


@pytest.mark.django_db
def test_categories(api_client):
    response = api_client.get(reverse("category"))
    assert response.status_code == status.HTTP_200_OK
