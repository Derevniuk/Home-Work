from functools import reduce

m = int(input('Input factorial number: '))


def reduce_func(el_pre: int, el: int) -> int:
    return el_pre * el


print(reduce(reduce_func, (a for a in range(1, m + 1))))
