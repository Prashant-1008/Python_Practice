from functools import lru_cache


def fib_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(maxsize=None)
def fib_memoized(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)


if __name__ == "__main__":
    for n in range(10):
        print(n, fib_recursive(n), fib_memoized(n)) 