# From a string of words, count how many times each word appears

s = "the world is yours the world is yours"

x = {i : s.count(i) for i in s.split()}

print(x)