def function_com(c):
    if len(c) == 0:
        return 'no one likes this'
    if len(c) == 1:
        return c[0] + ' likes this'
    if len(c) == 2:
        return c[0] + ' and ' + c[1] + ' like this'
    if len(c) == 3:
        return c[0] + ', ' + c[1] + ' and ' + c[2] + ' like this'
    if len(c) >= 4:
        return c[0] + ', ' + c[1] + ' and ' + str(len(c) + 1) + ' others like this'


print(function_com(["Alex", "Jacob", "Mark", "Max"]))
