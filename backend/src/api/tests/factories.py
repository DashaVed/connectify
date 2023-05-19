import factory

from web.models import User, Category, Group, Meeting


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    city = factory.Faker("city")
    name = factory.Faker("name")
    password = factory.Faker("password")

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


class MeetingFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('name')
    location = factory.Faker("address")
    description = factory.Faker('text')
    date = factory.Faker("date_time")
    group = factory.SubFactory(GroupFactory)

    class Meta:
        model = Meeting


