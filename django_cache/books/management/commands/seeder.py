from django_seed import Seed
from books.models import Author, Book, Library, BookData

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        This command seeds the database with fake data for testing purposes.
        It creates 1000 authors, 5 libraries, and 5000 book data entries.
        """

        Author.objects.all().delete()
        Library.objects.all().delete()
        BookData.objects.all().delete()
        Book.objects.all().delete()

        seeder = Seed.seeder()

        seeder.add_entity(Author, 1000, {
            "name": lambda x: seeder.faker.name()
        })

        seeder.add_entity(Library, 5, {
            'name': lambda x: seeder.faker.company(),
            'address': lambda x: seeder.faker.address(),
        })

        seeder.add_entity(BookData, 5000, {
            "title": lambda x: seeder.faker.sentence(nb_words=3, variable_nb_words=True),
            'isbn': lambda x: seeder.faker.isbn13(),
            "isbn_not_unique": lambda x: seeder.faker.isbn13(),
            'published_date': lambda x: seeder.faker.date_between(start_date='-50y', end_date='today'),
            'page_count': lambda x: seeder.faker.random_int(min=10, max=1000),
        })

        seeder.add_entity(Book, 7000)

        seeder.execute()
        # set_authors_m2m()

