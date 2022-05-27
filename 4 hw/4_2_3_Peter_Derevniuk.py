a = [1, 2, 3, 4, 5, 6]
b = [2, 4, 5, 6]

for e in b:
    if a.count(e):
        for r in a:
            if r == e:
                a.remove(r)

print(a)
