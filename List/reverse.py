nums = [1, 2, 3, 4, 5]

for i in range(len(nums)//2):
    nums[i] , nums[len(nums)-i-1] = nums[len(nums)-i-1] , nums[i]

print(nums)