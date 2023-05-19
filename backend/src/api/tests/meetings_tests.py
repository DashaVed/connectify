from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_meetings(api_client):
    response = api_client.get(reverse("meetings-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_meeting_create_without_user(api_client, group):
    payload = {
        "title": "test",
        "location": "Kazan",
        "date": datetime.now(),
        "is_online": False,
        "description": "test test test",
        "groups": group,
    }
    response = api_client.post(reverse("meetings-list"), data=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content


@pytest.mark.django_db
def test_meeting_detail(api_client, meeting):
    response = api_client.get(reverse("meetings-detail", args=(meeting.id, )))
    assert response.status_code == status.HTTP_200_OK
    assert meeting.id == response.json()["id"]


@pytest.mark.django_db
def test_meeting_partial_update(api_client, meeting):
    response = api_client.put(reverse("meetings-detail", args=(meeting.id,)), data={"title": "new_title"})
    assert response.status_code == status.HTTP_200_OK, response.content
    meeting.refresh_from_db()
    assert meeting.title == "new_title"
