# From this list of tuples, make a dictionary

pairs = [('a', 1), ('b', 2), ('c', 3)]

x = {i[0] : i[1] for i in pairs}

print(x)