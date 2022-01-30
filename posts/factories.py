import factory
from faker import Factory

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "auth.User"
        django_get_or_create = ('email',)

    email = factory.Sequence(lambda n: f'user-{n}@pywww.pl')
    username = factory.Sequence(lambda n: f'user{n}')
    password = "123"


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "posts.Post"

    title = factory.Sequence(lambda n: f'post {n}')
    content = factory.Sequence(lambda n: f'Lorem ipsum {n}')
    published = factory.LazyAttribute(lambda x: faker.boolean())
    sponsored = factory.LazyAttribute(lambda x: faker.boolean())
    author = factory.SubFactory(UserFactory)
    image = factory.django.FileField(filename="image.png")