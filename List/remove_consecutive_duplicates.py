nums = [1, 1, 2, 2, 3, 2, 2, 4]
x = []

for i in range(len(nums)):
    if i == 0 or nums[i] != nums[i-1]:
        x.append(nums[i])

print(x) 
