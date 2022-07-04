import sys


def fib_generator(n) -> list:
    d = []
    a, b = 1, 1
    for c in range(n):
        yield a
        d.append(a)
        a, b = b, a + b
    return d


def fib(n) -> list:
    d = [1]
    a, b = 1, 1
    for c in range(n - 1):
        a, b = b, a + b
        d.append(a)
    return d


print(sys.getsizeof(fib(10000)))
print(sys.getsizeof(fib_generator(10000)))

print(type(fib(10000)))
print(type(fib_generator(10000)))


