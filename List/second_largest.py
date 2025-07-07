nums = [5, 1, 8, 3, 9, 6]
x , y= float('-inf')
for i in nums:
    if i > x and i > y:
        y = x
        x = i

print(y)