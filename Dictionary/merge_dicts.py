#  You have a list of dictionaries. Merge them into one.

lst = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]

d = {}

for i in lst:
    d.update(i)

print(d)