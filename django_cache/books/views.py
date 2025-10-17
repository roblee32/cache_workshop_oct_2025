from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Book, Library


def uncached_view(request):
    books = Book.objects.all()
    return render(
        request,
        "books/list_books.html",
        {"books": books}
    )


##### View level Caching

@cache_page(60)
def cached_view(request):
    return uncached_view(request)


#### Template level Caching

def cached_template(request):
    books = Book.objects.all()
    return render(
        request,
        "books/cached_template.html",
        {"books": books}
    )


def another_view_using_cached_fragment(request):
    books = Book.objects.all()
    libraries = Library.objects.all()
    return render(
        request,
        "books/another_cached_template.html",
        {
            "books": books,
            "libraries": libraries
        }
    )


##### Fine Grained Caching

from django.core.cache import cache

def fine_grained_cache(request):
    cache_key = "books_cache"

    # Get data from the cache
    cached_data = cache.get(cache_key)

    # Check if there is data already
    if cached_data is None:
        books = Book.objects.all()
        # send data to the cache
        cache.set(cache_key, books, timeout=45)
    else:
        books = cached_data

    return render(
        request,
        "books/list_books.html",
        {"books": books}
    )
