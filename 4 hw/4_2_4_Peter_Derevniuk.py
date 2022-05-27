a = [61, 228, 91, 9, 10]
p = []
b = []

for n in a:
    b.append(str(n))
c = 0
for n in b:

    if int(n[0]) >= c:
        p.insert(0, n)
        c = int(n[0])
    if int(n[0]) < c:
        p.append(n)
        c = int(n[0])

print(''.join(p))
