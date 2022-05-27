number = input('Input: ')
i = 0
while i <= len(number):
    sum_number = 0
    for t in number:
        sum_number += int(t)
    number = str(sum_number)
    i += 1
print(number)
