import factory

from web.models import User, Category, Group


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    city = factory.Faker("city")
    name = factory.Faker("name")

    class Meta:
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('name')

    class Meta:
        model = Category


class GroupFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('name')
    city = factory.Faker("city")
    description = factory.Faker('text')

    class Meta:
        model = Group

