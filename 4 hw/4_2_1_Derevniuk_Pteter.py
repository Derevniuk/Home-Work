n = int(input('Input number: '))

b = 2
while n % b != 0:
    b += 1

if b == n:
    print(True)
else:
    print(False)
