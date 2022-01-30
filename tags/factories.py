import factory


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "tags.Tag"

    name = factory.Sequence(lambda n: f'tag-{n}')
    slug = factory.Sequence(lambda n: f'tag-{n}')
