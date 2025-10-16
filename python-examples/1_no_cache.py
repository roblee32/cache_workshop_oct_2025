from time import perf_counter

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    start = perf_counter()

    print(fib(35))

    end = perf_counter()

    print(f"{end - start} seconds")