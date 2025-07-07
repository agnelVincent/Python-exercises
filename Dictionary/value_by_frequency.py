# Group values by frequency

nums = [1, 2, 1, 3, 2, 1]

x = {i : [j for j in nums if j == i] for i in nums}

print(x)