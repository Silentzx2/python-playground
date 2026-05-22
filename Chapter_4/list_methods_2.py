names = ["Alice", "Bob", "Charlie", "David", 25, 3.14, True]
print(names)# Initialize a list with mixed data types
# Print the initial list
print(names)
# Append a string to the end of the list
names.append("Eve")
# Print the list after appending
print(names)
# Extend the list with another list
names.extend(["Frank", "Grace"])
# Print the list after extending
print(names)
# Insert a string at index 2
names.insert(2, "Helen")
# Print the list after inserting
print(names)
# Remove the first occurrence of 25
names.remove(25)
# Print the list after removing
print(names)
# Reverse the order of the list
names.reverse()
# Print the list after reversing
print(names)
# Sort the list (this will raise an error due to mixed data types)