def nok(x: int, y: int) -> int:
    c = 1
    z = True
    while z:
        if (x * c) % y == 0:
            z = False
            return (x * c)
        c += 1


print(nok(21, 28))
