# The values enter later will be updated to the same key
set = {1, 2, 3, 4, 5, [1,2]}
set[5][0] = 6 # You can't change the value of a set because it is immutable
# TypeError: unhashable type: 'list'
print(type(set))
