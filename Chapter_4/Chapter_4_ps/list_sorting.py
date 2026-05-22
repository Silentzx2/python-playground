a = (2, 5, 8, 1, 9, "Hello", 3.14, False)
a[5] = "World"  # This would cause an error since tuples are immutable
# TypeError: 'tuple' object does not support item assignment
print(a)  # Print the tuple