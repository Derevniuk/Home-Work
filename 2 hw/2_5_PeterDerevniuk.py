#Удаляет первый и послений символ в строке
b = input("Введите символы: ")
c = len(b)
b = list(b)
if c >= 3:
    b.pop()
    b[0] = ''
else:
    print("Вы ввели менее 2 символов")

print("Строка с удаленными элементами: " , "".join(b))

