#  Example of dictionary in Python
#  A dictionary is a collection of key-value pairs. Each key is unique and maps to
#  a value. Dictionaries are mutable, meaning you can change their contents after
#  they have been created.
mark = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}
print(mark, type(mark))  # Print the dictionary and its type
# Accessing values using keys
print("Alice's mark:", mark["Alice"])

print("""
Module for demonstrating dictionary usage and properties in Python.

A dictionary is a collection of key-value pairs where:
- Each key is unique and immutable (typically strings or numbers)
- Each key maps to a corresponding value
- Dictionaries are mutable (can be modified after creation)
- Dictionaries are unordered (maintain insertion order in Python 3.7+)
- Dictionaries are accessed using keys, not indices
- Dictionaries use curly braces {} for definition
- Key-value pairs are separated by colons (:)

Properties of Dictionaries in Python:
1. Mutable: Can add, remove, or modify key-value pairs after creation
2. Ordered: Preserves insertion order (Python 3.7+)
3. Indexed: Accessed via keys rather than numeric indices
4. Unique Keys: No duplicate keys allowed; later values overwrite earlier ones
5. Flexible Values: Values can be of any data type (int, str, list, etc.)
6. Dynamic Size: Can grow or shrink during program execution
7. Efficient Lookup: Keys provide O(1) average time complexity for access

Example:
    mark = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
    Accessing: mark["Alice"] returns 85
    Type: <class 'dict'>
""")