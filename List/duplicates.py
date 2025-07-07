nums = [1, 2, 3, 2, 4, 1, 5]

x = []

for i in range(len(nums)-1):
    if nums[i] in x:
        continue
    for j in range(i+1 , len(nums)):
        if nums[i] == nums[j]:
            x.append(nums[i])
            break

print(x)