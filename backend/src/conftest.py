import pytest
from rest_framework.test import APIClient

from api.tests.factories import UserFactory, GroupFactory, CategoryFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def group():
    return GroupFactory()


@pytest.fixture
def category():
    return CategoryFactory()
