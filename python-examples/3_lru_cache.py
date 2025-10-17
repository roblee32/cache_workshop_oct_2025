from time import perf_counter
from functools import lru_cache



# The LRU (Least Recently Used) cache is a decorator that can be applied to functions
# The main difference to @cache is that it has a max size
# This means that when the cache is full, the least recently used items are discarded
# This prevents the cache from growing indefinitely

@lru_cache(maxsize=8)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    start = perf_counter()

    print(fib(35))

    end = perf_counter()

    print(f"{end - start} seconds")

    print(fib.cache_info())

