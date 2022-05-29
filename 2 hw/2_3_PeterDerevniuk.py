#Проверка строки на палиндромность
b = input("Введите число: ")
r = 0
p = 0

for i in b:
    w = len(b) - 1
    if b[r] == b[w - r]:
        continue
    else:
        p += 1
    r = 1 + r

if p != 0:
    print('Не палиндром!')
else:
    print('Палиндром!')