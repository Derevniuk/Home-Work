a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
d = []
if a >= b:
    print('Введите корректно числа')
else:
    while a <= b:
        if a % 5 != 0:
            d.append(a)
        a += 1
print(len(d))
