import factory
from faker import Factory

from posts.factories import UserFactory

faker = Factory.create()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Author"
        django_get_or_create = ("name", "birth_year")

    name = factory.LazyAttribute(lambda x: faker.name())
    birth_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    biogram = factory.LazyAttribute(lambda x: faker.text(200))


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Book"

    title = factory.LazyAttribute(lambda x: faker.text(100))
    description = factory.LazyAttribute(lambda x: faker.text(300))
    publication_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    available = factory.LazyAttribute(lambda x: faker.boolean())

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create: return
        if extracted:
            for author in extracted:
                self.authors.add(author)


class BorrowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Borrow"

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)