from time import perf_counter
from functools import cache

# cache stores the answer for each input
# so it doesn't have to be recalculated
# answers it's already calculated

@cache
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

