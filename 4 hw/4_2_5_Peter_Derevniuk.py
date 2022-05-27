#Калькулятор
a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = input('Введите операцию: / , *, +, - : ')

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print('Error')
