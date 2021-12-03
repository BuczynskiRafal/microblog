import time
from .models import Book
from faker import Faker
from random import randint

fake = Faker('pl-PL')


def create_fake_books(n=10):
    results = []
    for _ in range(n):
        date = fake.date_time()
        book = Book.objects.create(
            title=fake.text(randint(30, 80)),
            description=fake.text(randint(200, 1000)),
            publication_year=int(fake.year()),
            author=fake.name(),
            available=fake.boolean(),
        )
        results.append(book)
    return results
