d = input('Input: ').replace(' ', '')
v = {}
for i in d:
    v[i] = v.get(i, 0) + 1
sorted_tuples = sorted(v.items(), key=lambda item: item[1])

v_key = []
v_values = []

for key, values in sorted_tuples:
    v_key.insert(0, key)
    v_values.insert(0, values)

v.clear()
v = dict(zip(v_key[:3], v_values[:3]))

print(v)