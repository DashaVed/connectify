import pytest
from django.urls import reverse
from rest_framework import status

from web.models import User


@pytest.mark.django_db
def test_users(api_client):
    response = api_client.get(reverse("users-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_user_detail(api_client, user):
    response = api_client.get(reverse("users-detail", args=(user.id, )))
    assert response.status_code == status.HTTP_200_OK
    assert user.id == response.json()["id"]


@pytest.mark.django_db
def test_user_update(api_client, user):
    response = api_client.put(reverse("users-detail", args=(user.id, )), data={"email": "test.test@test.com"})
    assert response.status_code == status.HTTP_200_OK, response.content
    user.refresh_from_db()
    assert user.email == "test.test@test.com"


def auth_user(api_client):
    payload = {
        "name": "user",
        "city": "User",
        "email": "user@user.user",
        "password": "fdsarewq4321",
        "re_password": "fdsarewq4321"
    }
    user = api_client.post('/api/auth/users/', payload)

    token = api_client.post('/api/auth/jwt/create/', data={
        "email": user.data["email"],
        "password": "fdsarewq4321",
    })
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token.data["access"])

    return user.data["id"]


@pytest.mark.django_db
def test_user_change_password(api_client):
    user_id = auth_user(api_client)
    payload = {
        "old_password": "fdsarewq4321",
        "new_password": "fdsarewq"
    }
    response = api_client.put(reverse("change_password", args=(user_id, )), data=payload)
    user = User.objects.get(id=user_id)

    assert response.status_code == status.HTTP_200_OK
    assert user.check_password("fdsarewq") is True
