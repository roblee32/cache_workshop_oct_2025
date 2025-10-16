from django.db.models.functions import Substr
from django.test import TestCase
from django_seed import Seed
from ..models import BookData, Book, Author, Library

class ExerciseTestCase(TestCase):
    # Rewrite these test to pass
    
    @classmethod
    def setUpTestData(cls):
        # Set up the test data here
        seeder = Seed.seeder()
        seeder.add_entity(Author, 30, {
            "name": lambda x: seeder.faker.name()
        })

        seeder.add_entity(Library, 3, {
            'name': lambda x: seeder.faker.company(),
            'address': lambda x: seeder.faker.address(),
        })

        seeder.add_entity(BookData, 50, {
            "title": lambda x: seeder.faker.sentence(nb_words=3, variable_nb_words=True),
            'isbn': lambda x: seeder.faker.isbn13(),
            "isbn_not_unique": lambda x: seeder.faker.isbn13(),
            'published_date': lambda x: seeder.faker.date_between(start_date='-50y', end_date='today'),
            'page_count': lambda x: seeder.faker.random_int(min=10, max=1000),
        })

        seeder.add_entity(Book, 70)
        seeder.execute()


    def test_prefetch_related(self):
        with self.assertNumQueries(2):
            books = BookData.objects.all()
            for book_data in books:
                _ = book_data.title
                _ = [a for a in book_data.authors.all()]


    def test_select_related(self):
        with self.assertNumQueries(1):
            books = Book.objects.all()
            for book in books:
                _ = book.library.name


    def test_annotation(self):
        with self.assertNumQueries(1):
            books = BookData.objects.all()
            for book in books:
                author_count = book.authors.count()


    def test_aggregation(self):
        with self.assertNumQueries(1):
            for book in BookData.objects.all():
                book_count = book.books.count()


    def test_authors_with_third_letter_a(self):
        # find how many authors have a name where the third letter is 'a'
        # Bad way to find answer
        count_authors = 0
        for author in Author.objects.all():
            if author.name.lower()[2] == "a":
                count_authors += 1

        # your code here:
        # You might need to search for an appropriate DB function in the Django documentation
        with self.assertNumQueries(1):
            your_answer = 0
            self.assertEqual(count_authors, your_answer)
