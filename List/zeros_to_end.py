nums = [0, 1, 0, 3, 12]

x = len(nums)-1

for i in range(len(nums)):
    if nums[i] == 0 and i < x:
        nums[i] , nums[x] = nums[x] , nums[i]
        x -= 1

print(nums)
