a = input('Input number card: ')

if len(a) == 16 and a.isdigit():
    b = int(a)
    print(12 * '#' + a[-4:])
else:
    print('error')
