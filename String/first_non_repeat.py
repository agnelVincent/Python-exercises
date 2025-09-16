# First non repeating characeter in string

s = 'aabbcddeffghi'

for i in s:
    if s.count(i) == 1:
        print(i)
        break