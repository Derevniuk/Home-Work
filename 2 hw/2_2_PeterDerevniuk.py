#Проверка числа на четность
b = input("Введите число: ")


if b.isdigit():
    n = int(b) % 2
    if n != 0:
        print('Число', b, 'нечетное')
    else:
        print('Число', b, 'четное')
else:
    print("Вы ввели некоректное число")
