# Remove all keys from a dict whose value is None or ""

d = {'name': 'Tony', 'city': '', 'job': None, 'power': 'high'}

x = {i : j for i,j in d.items() if j}

print(x)