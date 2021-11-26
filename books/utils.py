import time

from .models import Book
from faker import Faker
from random import randint


def create_fake_post(n=10):
    fake = Faker('pl-PL')
    for _ in range(n):
        book = Book(
            title=fake.text(randint(30, 80)),
            description=fake.text(randint(200, 1000)),
            publication_year=fake.text(randint(1800, 2021)),
            author=fake.name(),
            available=fake.boolean(),
        )
        book.save()
        print('-'*30)
        print(f'created {_+1}')
        time.sleep(0.5)