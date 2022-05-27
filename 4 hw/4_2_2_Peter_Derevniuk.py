dict = {10: 3, 2: 9, 4: 5, 6: 4}
sorted_dict = {}

def sorted_num(r):
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
                break
    print(sorted_dict)

c = int(input("Выберете способ сортировки ---> 1 - убывание, 2 - возрастание: "))

if c == 1:
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_num(sorted_values)

elif c == 2:
    sorted_values = sorted(dict.values())
    sorted_num(sorted_values)

else:
    print('Error')

