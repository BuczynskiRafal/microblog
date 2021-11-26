from django.core.management.base import BaseCommand
from posts.utils import create_fake_posts


class Command(BaseCommand):
    help = 'Create fake posts. Type int value to create posts.'

    def handle(self, *args, **kwargs):
        create_fake_posts(
            kwargs.get('count')
        )
        self.stdout.write('Posts has been created')

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            type=int,
            default=10,
            dest='count',
            help='Amount of posts to generate'
        )