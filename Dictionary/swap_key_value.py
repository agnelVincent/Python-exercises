# Invert this dictionary (values → keys)

data = {'a': 1, 'b': 2, 'c': 3}

x = {val:k for k,val in data.items()}

print(x)