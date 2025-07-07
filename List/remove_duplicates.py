nums = [1, 2, 2, 3, 1, 4]

x = []

for i in nums:
    if i not in x:
        x.append(i)


print(x)