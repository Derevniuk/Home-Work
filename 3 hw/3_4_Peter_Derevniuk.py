a = input('Введите число: ')
b = list(a)
c = 0
i = 0
while i < len(b):
    c += int(b[i])**3
    i += 1
if c == int(a) or len(b) == 1:
    print('Число является нарциссическим')
else:
    print('Число не является нарциссическим')
