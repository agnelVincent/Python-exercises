# Given a list of names, return a dict mapping names to their lengths

names = ['tony', 'montana', 'scarface']

freq = {i : len(i) for i in names}

print(freq)