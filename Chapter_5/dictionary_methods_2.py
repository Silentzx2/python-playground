# Dictionary Methods Examples

# Create a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# keys() - returns all keys
print(my_dict.keys())

# values() - returns all values
print(my_dict.values())

# items() - returns key-value pairs
print(my_dict.items())

# get() - safely access a value
print(my_dict.get("name"))
print(my_dict.get("country", "Not found"))

# pop() - remove and return a value
age = my_dict.pop("age")
print(age)

# update() - add/update multiple items
my_dict.update({"age": 31, "country": "USA"})

# clear() - remove all items
# my_dict.clear()

# copy() - create a shallow copy
dict_copy = my_dict.copy()

# setdefault() - get value or set default
my_dict.setdefault("phone", "N/A")

print(my_dict)