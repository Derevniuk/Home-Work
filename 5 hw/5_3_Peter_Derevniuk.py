def sum_range(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    return sum([i for i in range(start, end + 1)])

print(sum_range(10, 20))
