import time

from .models import Post
from faker import Faker
from random import randint


def create_fake_posts(n=10):
    fake = Faker('pl-PL')
    for _ in range(n):
        create = fake.date_time()
        post = Post(
            title=fake.text(randint(10, 40)),
            content=fake.text(randint(200, 1000)),
            published=fake.boolean(),
            created=create,
            modified=create + fake.time_delta(),
            sponsored=fake.boolean(),
        )
        post.save()
        print('-'*30)
        print(f'created {_+1}')
        time.sleep(0.5)