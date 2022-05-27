s = 0


def sum_list(n: list) -> int:
    global s
    s += n[-1]
    n.pop(-1)
    if n:
        sum_list(n)
    return s


print(sum_list([1, 3, 4, 5, 7, 7, 8]))

