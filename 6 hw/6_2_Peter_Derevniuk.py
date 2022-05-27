import random


def random_number():
    return [random.randint(0, 9) for t in range(0, 12)]


def edit_number_tel(lst: list) -> str:
    b = ['+', lst[0], lst[1], lst[2], '(', lst[3], lst[4], ')', lst[5], lst[6], lst[7],
         '-', lst[8], lst[9], '-', lst[10], lst[11]]
    return "".join(map(str, b))


print(edit_number_tel(random_number()))
