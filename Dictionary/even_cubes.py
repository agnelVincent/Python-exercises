# Filter and create a dict of only even keys and their cubes

nums = [1, 2, 3, 4, 5]

even_cubes = {i : i**3 for i in nums if i%2==0}

print(even_cubes)