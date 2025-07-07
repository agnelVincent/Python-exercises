nums = [1, 2, 3, 2, 4, 2, 5]

n = int(input('enter number you want to delete'))

x = [i for i in nums if i!=n]

print(x)
