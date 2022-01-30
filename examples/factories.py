import factory
from factory import post_generation
from faker import Factory
from faker_vehicle import VehicleProvider
from examples.models import EngineTypes


faker = Factory.create()
faker.add_provider(VehicleProvider)


class EngineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'examples.Engine'
        django_get_or_create = ('capacity', 'power', 'engine_type')

    capacity = factory.LazyAttribute(lambda x: faker.random.randrange(1000, 3500, 500))
    power = factory.LazyAttribute(lambda x: faker.random.randrange(90, 220, 10))
    engine_type = factory.LazyAttribute(lambda x: faker.random.randint(1, 4))

    @post_generation
    def post(self, create, extracted, **kwargs):
        if self.engine_type in [EngineTypes.ELECTRIC, EngineTypes.OTHER]:
            self.capacity = None


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "examples.Car"

    brand = factory.LazyAttribute(lambda x: faker.vehicle_make())
    model = factory.LazyAttribute(lambda x: faker.vehicle_model())
    production_year = factory.LazyAttribute(lambda x: faker.vehicle_year())
    seats = factory.LazyAttribute(lambda x: faker.random.randint(2, 7))
    cost = factory.LazyAttribute(lambda x: faker.random.randint(5000, 100000))
    engine = factory.SubFactory(EngineFactory)
    millage = factory.LazyAttribute(lambda x: faker.random.randint(10, 100000))


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "tags.Tag"

    name = factory.Sequence(lambda n: f'tag-{n}')
    slug = factory.Sequence(lambda n: f'tag-{n}')
