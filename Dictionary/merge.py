# Merge two dictionaries. If same key, sum values

a = {'a': 10, 'b': 20}
b = {'b': 30, 'c': 40}

for key in b:
    a[key] = a.get(key , 0) + b[key]

print(a)