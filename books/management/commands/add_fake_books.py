from django.core.management.base import BaseCommand
from books.utils import create_fake_books


class Command(BaseCommand):
    help = "Create fake books. Type int value to create books."

    def handle(self, *args, **options):
        n = options.get("number", 10)
        books = create_fake_books(n)
        self.stdout.write(f"{len(books)} books was created.")

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--number',
            type=int,
            default=10,
            dest='number',
            help='Amount of books to generate'
        )
